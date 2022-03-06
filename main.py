import CaseStudy
import os

AccessData = CaseStudy.StudiKasus2(host="localhost" , port=3306 , user="root" , password=os.environ['PASS_MYSQL'])

print(AccessData.create_db("Tryout2"))

df = AccessData.import_csv("C:\\Users\\User-PC\\Desktop\\addresses.csv")

# print(df.firstName)

AccessData.create_table("Tryout2","user",df)

print(AccessData.load_data("Tryout2","user"))

