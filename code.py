import streamlit as st
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import time

def scrape_data(parcel_numbers, selected_fields, selected_domains):
    rows = []
    total_requests = len(parcel_numbers)
    start_time = time.time()

    for selected_domain in selected_domains:
        for idx, txroll_cadaccountnumber in enumerate(parcel_numbers, start=1):
            url = f'https://esearch.{selected_domain}/Property/View/{txroll_cadaccountnumber}?year=2023'
            r = requests.get(url)
            try:
                soup = BeautifulSoup(r.content, 'html.parser')
                # soup = soup.find_all('div', class_='panel panel-primary')[2].find_all('tr')


                # Initialize all fields to empty strings
                scraped_data = {
                    'Geographic_ID':'',
                    'Property_ID': '',
                    'Type': '',
                    'Situs_Address': '',
                    'Map_ID':'',
                    'Mapsco':'',
                    'Legal_Description':'',
                    'Abstract_Subdivision':'',
                    'Neighborhood':'',
                    'owner_ID':'',
                    'name':'',
                    'Agent':'',
                    'Mailing_Address':'',
                    'Ownership':'',
                    'Improvement_Homesite_Value':'',
                    'Improvement_Non_Homesite_Value': '',
                    'Land_Homesite_Value': '',
                    'Land_Non_Homesite_Value': '',
                    'Agricultural_Market_Valuation': '',
                    'Market_Value':''


                }
                if 'Geographic_ID' in selected_fields:
                    Geographic_ID = re.findall(
                        r'Geographic ID: <\/strong>[^<>]*', str(soup))
                    Geographic_ID = ' '.join(Geographic_ID)
                    Geographic_ID = re.sub('\s+', ' ', Geographic_ID)
                    Geographic_ID = Geographic_ID.split('Geographic ID:')[1].replace('</strong>', '').strip()
                    scraped_data['Geographic_ID'] = Geographic_ID

                if 'Property_ID' in selected_fields:
                    Property_ID = re.findall(
                        r'Property ID:<\/th>\s+<td class="tbltrwidth">[^<>]*', str(soup))
                    Property_ID = ' '.join(Property_ID)
                    Property_ID = re.sub('\s+', ' ', Property_ID)
                    Property_ID = Property_ID.split('Property ID:')[1].replace('</th> <td class="tbltrwidth">','').strip()
                    scraped_data['Property_ID'] = Property_ID
                if 'Type' in selected_fields:
                    Type = re.findall(
                        r'Type:<\/th>\s+<td>[^<>]*', str(soup))
                    Type = ' '.join(Type)
                    Type = re.sub('\s+', ' ', Type)
                    Type = Type.split('Type:')[1].replace('</th> <td>', '').strip()
                    scraped_data['Type'] = Type

                if 'Situs_Address' in selected_fields:
                    Situs_Address = re.findall(
                        r'Situs Address:<\/th><td colspan="3">[^<>]*', str(soup))
                    Situs_Address = ' '.join(Situs_Address)
                    Situs_Address = re.sub('\s+', ' ', Situs_Address)
                    Situs_Address = Situs_Address.split('Situs Address:')[1].replace('</th><td colspan="3">', '').strip()
                    scraped_data['Situs_Address'] = Situs_Address

                if 'Map_ID' in selected_fields:
                    Map_ID = re.findall(
                        r'Map ID:<\/th>\s+<td>[^<>]*', str(soup))
                    Map_ID = ' '.join(Map_ID)
                    Map_ID = re.sub('\s+', ' ', Map_ID)
                    Map_ID = Map_ID.split('Map ID:')[1].replace('</th> <td>', '').strip()
                    scraped_data['Map_ID'] = Map_ID

                if 'Mapsco' in selected_fields:
                    Mapsco = re.findall(
                        r'Mapsco: <\/strong>[^<>]*', str(soup))
                    Mapsco = ' '.join(Mapsco)
                    Mapsco = re.sub('\s+', ' ', Mapsco)
                    Mapsco = Mapsco.split('Mapsco:')[1].replace('</strong>', '').strip()
                    scraped_data['Mapsco'] = Mapsco

                if 'Legal_Description' in selected_fields:
                    Legal_Description = re.findall(
                        r'Legal Description:<\/th>\s+<td colspan="3">[^<>]*',
                        str(soup))
                    Legal_Description = ' '.join(Legal_Description)
                    Legal_Description = re.sub('\s+', ' ', Legal_Description)
                    Legal_Description = Legal_Description.split('Legal Description:')[1].replace('</th> <td colspan="3">',
                                                                                                 '').strip()
                    scraped_data['Legal_Description'] = Legal_Description

                if 'Abstract_Subdivision' in selected_fields:
                    Abstract_Subdivision = re.findall(
                        r'Abstract\/Subdivision:<\/th><td colspan="3">[^<>]*+',
                        str(soup))
                    Abstract_Subdivision = ' '.join(Abstract_Subdivision)
                    Abstract_Subdivision = re.sub('\s+', ' ', Abstract_Subdivision)
                    Abstract_Subdivision = Abstract_Subdivision.split('Abstract/Subdivision:')[1].replace(
                        '</th><td colspan="3">', '').strip()
                    scraped_data['Abstract_Subdivision'] = Abstract_Subdivision

                if 'Neighborhood' in selected_fields:
                    Neighborhood = re.findall(
                        r'Neighborhood:<\/th><td class="wordbreak" colspan="3">[^<>]*',
                        str(soup))
                    Neighborhood = ' '.join(Neighborhood)
                    Neighborhood = re.sub('\s+', ' ', Neighborhood)
                    Neighborhood = Neighborhood.split('Neighborhood:')[1].replace('</th><td class="wordbreak" colspan="3">',
                                                                                  '').strip()
                    scraped_data['Neighborhood'] = Neighborhood

                if 'owner_ID' in selected_fields:
                    owner_ID = re.findall(r'Owner ID:<\/th><td colspan="3">[^<>]*', str(soup))
                    owner_ID = ' '.join(owner_ID)
                    owner_ID = re.sub('\s+', ' ', owner_ID)
                    owner_ID = owner_ID.split('Owner ID:')[1].replace('</th><td colspan="3">', '').strip()
                    scraped_data['owner_ID'] = owner_ID

                if 'name' in selected_fields:
                    name = re.findall(r'Name:<\/th><td colspan="3">[^<>]*', str(soup))
                    name = ' '.join(name)
                    name = re.sub('\s+', ' ', name)
                    name = name.split('Name:')[1].replace('</th><td colspan="3">', '').strip()
                    scraped_data['name'] = name

                if 'Agent' in selected_fields:
                    Agent = re.findall(r'Agent:<\/th><td colspan="3">[^<>]*', str(soup))
                    Agent = ' '.join(Agent)
                    Agent = re.sub('\s+', ' ', Agent)
                    Agent = Agent.split('Agent:')[1].replace('</th><td colspan="3">', '').strip()
                    scraped_data['Agent'] = Agent


                if 'Mailing_Address' in selected_fields:
                    Mailing_Address = re.findall(r'Mailing Address:<\/th><td colspan="3">[^<>]*', str(soup))
                    Mailing_Address = ' '.join(Mailing_Address)
                    Mailing_Address = re.sub('\s+', ' ', Mailing_Address)
                    Mailing_Address = Mailing_Address.split('Mailing Address:')[1].replace('</th><td colspan="3">',
                                                                                           '').strip()
                    scraped_data['Mailing_Address'] = Mailing_Address


                if 'Ownership' in selected_fields:
                    Ownership = re.findall(r'Ownership:<\/th><td colspan="3">[^<>]*', str(soup))
                    Ownership = ' '.join(Ownership)
                    Ownership = re.sub('\s+', ' ', Ownership)
                    Ownership = Ownership.split('Ownership:')[1].replace('</th><td colspan="3">', '').strip()
                    scraped_data['Ownership'] = Ownership

                if 'Improvement_Homesite_Value' in selected_fields:
                    Improvement_Homesite_Value = re.findall(
                        r'Improvement Homesite Value:<\/th><td class="table-number">[^<>]*', str(soup))
                    Improvement_Homesite_Value = ' '.join(Improvement_Homesite_Value)
                    Improvement_Homesite_Value = re.sub('\s+', ' ', Improvement_Homesite_Value)
                    Improvement_Homesite_Value = Improvement_Homesite_Value.split('Improvement Homesite Value:')[1].replace(
                        '</th><td class="table-number">', '').strip()
                    scraped_data['Improvement_Homesite_Value'] = Improvement_Homesite_Value

                if 'Improvement_Non_Homesite_Value' in selected_fields:
                    Improvement_Non_Homesite_Value = re.findall(
                        r'Improvement Non-Homesite Value:<\/th><td class="table-number">[^<>]*', str(soup))
                    Improvement_Non_Homesite_Value = ' '.join(Improvement_Non_Homesite_Value)
                    Improvement_Non_Homesite_Value = re.sub('\s+', ' ', Improvement_Non_Homesite_Value)
                    Improvement_Non_Homesite_Value = \
                    Improvement_Non_Homesite_Value.split('Improvement Non-Homesite Value:')[1].replace(
                        '</th><td class="table-number">', '').strip()
                    scraped_data['Improvement_Non_Homesite_Value'] = Improvement_Non_Homesite_Value

                if 'Land_Homesite_Value' in selected_fields:
                    Land_Homesite_Value = re.findall(r'Land Homesite Value:<\/th><td class="table-number">[^<>]*',
                                                     str(soup))
                    Land_Homesite_Value = ' '.join(Land_Homesite_Value)
                    Land_Homesite_Value = re.sub('\s+', ' ', Land_Homesite_Value)
                    Land_Homesite_Value = Land_Homesite_Value.split('Land Homesite Value:')[1].replace(
                        '</th><td class="table-number">', '').strip()
                    scraped_data['Land_Homesite_Value'] = Land_Homesite_Value

                if 'Land_Non_Homesite_Value' in selected_fields:
                    Land_Non_Homesite_Value = re.findall(r'Land Non-Homesite Value:<\/th><td class="table-number">[^<>]*',
                                                         str(soup))
                    Land_Non_Homesite_Value = ' '.join(Land_Non_Homesite_Value)
                    Land_Non_Homesite_Value = re.sub('\s+', ' ', Land_Non_Homesite_Value)
                    Land_Non_Homesite_Value = Land_Non_Homesite_Value.split('Land Non-Homesite Value:')[1].replace(
                        '</th><td class="table-number">', '').strip()
                    scraped_data['Land_Non_Homesite_Value'] = Land_Non_Homesite_Value

                if 'Agricultural_Market_Valuation' in selected_fields:
                    Agricultural_Market_Valuation = re.findall(
                        r'Agricultural Market Valuation:<\/th><td class="table-number">[^<>]*', str(soup))
                    Agricultural_Market_Valuation = ' '.join(Agricultural_Market_Valuation)
                    Agricultural_Market_Valuation = re.sub('\s+', ' ', Agricultural_Market_Valuation)
                    Agricultural_Market_Valuation = Agricultural_Market_Valuation.split('Agricultural Market Valuation:')[
                        1].replace('</th><td class="table-number">', '').strip()
                    scraped_data['Agricultural_Market_Valuation'] = Agricultural_Market_Valuation

                if 'Market_Value' in selected_fields:
                    Market_Value = re.findall(r'Market Value:<\/th><td class="table-number">[^<>]*', str(soup))
                    Market_Value = ' '.join(Market_Value)
                    Market_Value = re.sub('\s+', ' ', Market_Value)
                    Market_Value = Market_Value.split('Market Value:')[1].replace('</th><td class="table-number">', '').strip()
                    scraped_data['Market_Value'] = Market_Value



                row_dict = {'domain': selected_domain, 'parcel_number': txroll_cadaccountnumber, **scraped_data}
                rows.append(row_dict)

                # Display estimated time remaining
                elapsed_time = time.time() - start_time
                avg_time_per_request = elapsed_time / idx if idx > 0 else 0
                remaining_requests = total_requests - idx
                estimated_time_remaining = avg_time_per_request * remaining_requests

                st.markdown(f"<p style='color: green;'>Estimated time remaining: {round(estimated_time_remaining, 2)} seconds  {idx} completed</p>",
                            unsafe_allow_html=True)

            except Exception as e:
                st.warning(f"Failed to fetch data for parcel number {txroll_cadaccountnumber} on domain {selected_domain}: {str(e)}")
                # Set all selected fields to empty strings
                scraped_data = {field: '' for field in selected_fields}

            # Append the row_dict to the rows list

    result_df = pd.DataFrame(rows)
    return result_df

def main():


    st.title('Esearch Site Property Scraper')
    st.write("Upload an Excel file containing 'parcel_number' column.")

    uploaded_file = st.file_uploader("Upload Excel file", type=['xlsx', 'xls'])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            parcel_numbers = df['parcel_number'].tolist()

            # Define available fields for selection
            available_fields = ['Select All','Geographic_ID','Property_ID','Type','Situs_Address','Map_ID','Mapsco','Legal_Description','Abstract_Subdivision','Neighborhood','owner_ID','name','Agent','Mailing_Address','Ownership','Improvement_Homesite_Value','Improvement_Non_Homesite_Value','Land_Homesite_Value','Land_Non_Homesite_Value','Agricultural_Market_Valuation','Market_Value']  # Add more fields here

            # Checkbox options for selecting fields
            selected_fields = st.multiselect('Select Fields for Output', available_fields)

            # Define available domains for selection
            list2 = ['dallamcad.org','delta-cad.org','fallscad.net','galvestoncad.org','bastropcad.org']
            selected_domains = st.multiselect('Select Domains', list2)

            # Check if 'Select All' is chosen and update selected_fields accordingly
            if 'Select All' in selected_fields:
                selected_fields = available_fields[1:]  # Exclude the 'Select All' option

            if st.button('Scrape Data'):
                scraped_data = scrape_data(parcel_numbers, selected_fields, selected_domains)
                st.write(scraped_data)

                # Download the output file
                csv = scraped_data.to_csv(index=False)
                st.download_button(label="Download Output", data=csv, file_name='scraped_data.csv',
                                   mime='text/csv')

        except Exception as e:
            st.warning(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
