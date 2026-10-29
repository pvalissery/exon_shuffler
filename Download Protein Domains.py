#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:12:00 2026

@author: praveeshvalissery
"""

import requests
import pandas as pd
import os
import re

def download_all_domain_names():
    # Direct HTTPS link to the stable flat-file database dump on the EMBL-EBI FTP mirror
    url = "https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/entry.list"
    
    accessions = []
    names = []
    
    print("Connecting directly to the EMBL-EBI FTP repository... Please wait...")
    print("Streaming the complete unified database catalog...")
    
    try:
        # Stream the file line-by-line
        response = requests.get(url, stream=True, timeout=45)
        response.raise_for_status()
        
        for raw_line in response.iter_lines():
            if not raw_line:
                continue
            
            # Explicitly decode raw bytes to a text string safely
            line = raw_line.decode('utf-8', errors='ignore').strip()
            
            # Skip comments and header lines
            if line.startswith('#') or line.startswith('ENTRY_ACC'):
                continue
                
            # Split line using a robust regex that matches tabs OR 2+ consecutive spaces
            parts = re.split(r'\t|\s{2,}', line)
            
            if len(parts) >= 3:
                accession = parts[0].strip()
                entry_type = parts[1].strip()
                # Join any remaining elements if the name itself contained multiple spaces
                name = " ".join([p.strip() for p in parts[2:] if p.strip()])
                
                # Filter out entries specifically categorized as a 'Domain'
                if entry_type.lower() == 'domain':
                    accessions.append(accession)
                    names.append(name)
                    
        print(f"Parsing complete! Successfully extracted {len(accessions)} domain records.")
        
    except requests.exceptions.RequestException as e:
        print(f"\nNetwork connection failed: {e}")
        return
    except Exception as e:
        print(f"\nAn error occurred while reading the flat-file: {e}")
        return

    # Compile the final lists into a structured Excel table
    if accessions:
        df = pd.DataFrame({
            'Accession': accessions,
            'Domain_Name': names
        })
        
        output_path = "/Users/praveeshvalissery/Downloads/domain.xlsx"
        
        # Verify and build destination directory paths if missing
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        print("Writing records to Excel spreadsheet...")
        df.to_excel(output_path, index=False, engine='openpyxl')
        print(f"Success! All domain names successfully saved to: {output_path}")
    else:
        print("\nProcess finished, but no domain profiles matched the search parameters.")

if __name__ == "__main__":
    download_all_domain_names()
