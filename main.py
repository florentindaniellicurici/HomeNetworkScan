import scanet
import networkdetails
import expToJson


yourip, networkip = networkdetails.networkdetails()
print(networkip)
dict = scanet.scan(networkip)

expToJson.export_to_json_file(dict)




