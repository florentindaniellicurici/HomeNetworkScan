import scanet
import networkdetails


yourip, networkip = networkdetails.networkdetails()
print(networkip)
dict = scanet.scan(networkip)




