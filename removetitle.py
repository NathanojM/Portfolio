import os

def remove_title(filename):
    file=open(filename,"r")
    title=filename.replace(".html","")
    newfilename=f"new{filename}"
    newfile=open(newfilename,"w")
    
    linea='<h1 class="page-title heading" id="'
    lineb='">'
    linec="</h1>"
    line=f"{linea}{title}{lineb}{title}{linec}"
    

    for x in file.readlines():
        if line in x:
            
            newfile.write(x.replace(line,""))
            
        else:
            newfile.write(x)
    newfile.write("\n")
    file.close()
    newfile.close()

    os.system(f"rm {filename}")
    os.system(f"mv {newfilename} {filename}")
    print(f"{filename}✅")

for x in os.listdir("."):
    if x.endswith(".html") and not x.startswith("head"):
        remove_title(x)
        pass
