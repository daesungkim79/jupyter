#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup as Soup


# In[108]:


#handler = open("ActrMot.arxml").read()
#handler = open("GateDrvr.arxml").read()
#handler = open("ApplComPrivate.arxml").read()
handler = open("IntPwrSply.arxml").read()

#soup = Soup(handler, 'html.parser')
soup = Soup(handler, 'xml')
#soup


# In[111]:


#dest = [d.text for d in soup.find_all("APPLICATION-DATA-TYPE-REF") if d["DEST"] == "APPLICATION-PRIMITIVE-DATA-TYPE"]
d_1 = soup.find_all("APPLICATION-SW-COMPONENT-TYPE")
d_2 = soup.find_all("ECU-ABSTRACTION-SW-COMPONENT-TYPE")

#print(d_1)

p_port_ls = []
r_port_ls = []

for e_1 in d_1:
    #var_ls.append(d.split('ApplicationDataTypes/')[-1])
    d_p_port = e_1.find_all("P-PORT-PROTOTYPE")
    d_r_port = e_1.find_all("R-PORT-PROTOTYPE")
    for e_p_port in d_p_port:
        #p_port_ls.append([d.text for d in e_p_port.find_all("L-4") if d["L"] == "EN"])
        p = [d.text for d in e_p_port.find_all("SHORT-NAME")]
        p_port_ls.append(p)

    for e_r_port in d_r_port:
        #r_port_ls.append([d.text for d in e_r_port.find_all("L-4") if d["L"] == "EN"])        
        r = [d.text for d in e_r_port.find_all("SHORT-NAME")]
        r_port_ls.append(r)

for e_1 in d_2:
    #var_ls.append(d.split('ApplicationDataTypes/')[-1])
    d_p_port = e_1.find_all("P-PORT-PROTOTYPE")
    d_r_port = e_1.find_all("R-PORT-PROTOTYPE")
    for e_p_port in d_p_port:
        #p_port_ls.append([d.text for d in e_p_port.find_all("L-4") if d["L"] == "EN"])
        p = [d.text for d in e_p_port.find_all("SHORT-NAME")]
        p_port_ls.append(p)

    for e_r_port in d_r_port:
        #r_port_ls.append([d.text for d in e_r_port.find_all("L-4") if d["L"] == "EN"])        
        r = [d.text for d in e_r_port.find_all("SHORT-NAME")]
        r_port_ls.append(r)        
        

print("P-PORTS: ", len(p_port_ls))
print("R-PORTS: ", len(r_port_ls))
print(p_port_ls)
print(r_port_ls)


# In[ ]:





# In[112]:


from openpyxl import load_workbook


# In[164]:


def analyzeBaseData(swcName):
    df = pd.read_excel("baseData.xlsx")

    data = df[df["swcName"] == swcName].reset_index(drop=True)
    expVal = data.loc[0, "months of experience"]
    impactRng = data.loc[0, "Impact range"]

    return expVal, impactRng


# In[167]:


data1, data2 = analyzeBaseData("ActrMot")
print(data1, data2)


# In[ ]:




