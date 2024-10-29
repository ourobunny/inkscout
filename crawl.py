import sys
import shodan

api_key = "0ZFjUoFZYMk8XUeRDV32ukNPk6vWahdo"
api = shodan.Shodan(api_key)

file = open("results.txt", "w")


processed = {}

def crawl_canada():
    results = api.search(query = 'port:9100 @PJL HP country:"CA"')

    for r in results["matches"]:
        file.write("IP: " + r["ip_str"])
        file.write("\nLocation: " + str(r["location"]["city"] or "None") + ", " + r["location"]["country_name"])
        file.write("\nProduct: " + str(r["product"] or "None"))
        file.write("\nOrganization: " + str(r["org"]or "None") + "\n\n")

    global totalf
    totalf = results["total"]

def crawl_world():
    results = api.search(query = 'port:9100 @PJL HP')

    for r in results["matches"]:
        file.write("IP: " + r["ip_str"])
        file.write("\nLocation: " + str(r["location"]["city"] or "None") + ", " + r["location"]["country_name"])
        file.write("\nProduct: " + str(r["product"] or "None"))
        file.write("\nOrganization: " + str(r["org"]or "None") + "\n\n")
    
    global totalf
    totalf = results["total"]   

  

if sys.argv[1] == "1":
    crawl_canada()
    print("\nDone! Found " + str(totalf) + " unsecured printers in total.")


elif sys.argv[1] == "2":
    crawl_world()
    print("\nDone! Found " + str(totalf) + " unsecured printers in total.")




file.close()