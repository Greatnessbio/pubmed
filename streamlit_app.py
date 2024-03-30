import streamlit as st
import pandas as pd
from async_pubmed_scraper import PubMedScraper, parse_args
import numpy as np
import pandas as pd

def app():
    st.title("Asynchronous PubMed Scraper")

    # Get user input
    keywords = st.text_area("Enter keywords (one per line)")
    start_year = st.number_input("Start year", min_value=1900, value=2019)
    end_year = st.number_input("End year", min_value=1900, value=2020)
    num_pages = st.number_input("Number of pages", min_value=1)
    output_file = st.text_input("Output file name", value="articles.csv")

    # Create a button to trigger the scraping process
    if st.button("Scrape PubMed"):
        # Parse user input into command-line arguments
        args = parse_args([
            "--pages", str(num_pages),
            "--start", str(start_year),
            "--stop", str(end_year),
            "--output", output_file,
            "--keywords", keywords.replace("\n", ",")
        ])

        # Create a PubMedScraper instance and run the scraping
        scraper = PubMedScraper(args)
        data = scraper.run()

        # Convert the data to a Pandas DataFrame
        df = pd.DataFrame(data)

        # Display the scraped data
        st.write(df)

# Run the Streamlit app
if __name__ == "__main__":
    app()
