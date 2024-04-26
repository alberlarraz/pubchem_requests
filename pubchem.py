import pubchempy as pcp
import csv
import pandas as pd

csv_list = []
with open('C2.csv', newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    result = pd.read_csv('C2.csv')
    total_rows = len(result)

#From NAME to CID & ISOMERIC SMILES
    #for count, row in enumerate(reader):
        #compound = pcp.get_compounds(row[0], 'name')
        #cid = pcp.get_cids(row[0], 'name')
        #print("Calculando...", count, "de", total_rows)
        #if compound != []:
            #csv_list.append((row, cid, compound[0].isomeric_smiles))
        #else:
            #csv_list.append((row, "", ""))

#From CID to ISOMERIC SMILES
    #for count, row in enumerate(reader):
        #compound = pcp.get_compounds(row[0], 'cid')
        #print("Calculando...", count, "de", total_rows)
        #if compound != []:
            #csv_list.append((row, compound[0].isomeric_smiles))
        #else:
            #csv_list.append((row, "", ""))

#From CID to NAME
    #for count, row in enumerate(reader):
        #compound = pcp.get_compounds(row[0], 'cid')
        #print("Calculando...", count, "de", total_rows)
        #if compound != []:
            #csv_list.append((row, compound[0].iupac_name))
        #else:
            #csv_list.append((row, "", ""))            

#From SMILES to NAME & CID
    for count, row in enumerate(reader):
        print(row)
        if row == []:
            compound = []
        else:
            compound = pcp.get_compounds(row[0], 'smiles')
            cid = pcp.get_cids(row[0], 'smiles')
            print("Calculando...", count, "de", total_rows)

            if compound != []:
                csv_list.append((row, compound[0].iupac_name, cid))
            else:
                csv_list.append((row, "", ""))

            with open('newdata.csv', 'a', newline='\n') as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                for info in csv_list:
                    writer.writerow(info)
                csv_list.clear()


#with open('newdata.csv', 'w', newline='\n') as csvfile:
    #writer = csv.writer(csvfile, delimiter=",")
    #for info in csv_list:
        #writer.writerow(info)

