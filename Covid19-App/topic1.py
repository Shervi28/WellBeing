from time import sleep
from os import system, name 
from rich.console import Console
from pyfiglet import Figlet, figlet_format

console = Console()

def clear2(): 
  
  if name == 'nt': 
       
    _ = system('cls') 
    
  else: 
       
    _ = system('clear') 

def main():
  console.print("[red]What should I help you with?[/red]")
  print("\n")
  sleep(1)
  console.print("1.[blue]Heart Diseases[/blue]")
  console.print("[blue]2.Cancer[/blue]")
  console.print("[blue]3.Diabetes[/blue]")
  console.print("[blue]4.Stroke[/blue]")
  
  print("\n")
  topics1=int(input("Enter a number:"))
  
  print("\n")
  if topics1 == 1:
    console.print("[red]1.Congenital Heart Disease")
    console.print("[orange]2.Coronary Artery Disease")
    console.print("[green]3.Heart Arrhythmia")
    console.print("[blue]4.Dilated Cardiomyopathy")
    print("\n")
    topics2=input("Enter a number:")

    

    
  if topics1 == 2:
    console.print("[yellow]1.Breast Cancer[/yellow]")
    console.print("[blue]2.Lung Cancer[/blue]")
    console.print("[orange]3.Prostate Cancer[/orange]")
    console.print("\n")
    topics2=input("Enter a number:")
    
    

  if topics1 == 3:
    console.print("[red]1.Type Diabities[/red]")
    console.print("[magenta]2.Type Diabities[/magenta]")
    console.print("\n")
    topics2=input("Enter a number:")
    
    

  if topics1 == 4:
    console.print("[blue]1.Ischaemic Stroke[/blue]")
    console.print("[green]2.Haemorrhagic Stroke[/green]")
    console.print("[yellow]3.Transient ischaemic attack Stroke[/yellow]")
    console.print("\n")
    topics2=input("Enter a number:")

  

  print("\n")
  

  if(topics1==1 and topics2=="1"):
    console.print("[yellow]Treatments include medications to lower blood pressure and control heart rate, heart devices, catheter procedures, and surgery. Serious cases may require a heart transplant.[/yellow]")
    sleep(10)
    
  elif(topics1==1 and topics2=="2"):
    console.print("[yellow]Quitting smoking, Weight loss, Physical exercise, and Low fat diet.[/yellow]")
    sleep(10)
    
  elif(topics1==1 and topics2=="3"):
    console.print("[magenta]If needed, treatment includes anti-arrhythmic drugs, medical procedures, implantable devices, and surgery.[/magenta]")
    sleep(10)
  

  if(topics1==1 and topics2=="4"):
    console.print("[purple]Don't smoke. Don't drink alcohol, or drink in moderation. Don't use cocaine or other illegal drugs. Eat a healthy diet that is low in salt (sodium). Maintain a healthy weight. Follow an exercise program recommended by your doctor. Get enough sleep and rest. Manage stress.[/purple]")
    sleep(10)
    
  if(topics1==2 and topics2=="1"):
    console.print("[green]Surgery.[/green]")
    sleep(10)

  if(topics1==2 and topics2=="2"):
    console.print("[orange]Treatments vary but may include surgery, chemotherapy, radiation therapy, targeted drug therapy, and immunotherapy.[/orange]")
    sleep(10)
    
  if(topics1==2 and topics2=="3"):
    console.print("[yellow]Active Surveillance, surgery, and radiation therapy.[/yellow]")
    sleep(10)

  if(topics1==3 and topics2=="1"):
    console.print("[blue]Treatment aims at maintaining normal blood sugar levels through regular monitoring, insulin therapy, diet, and exercise.[/blue]")
    sleep(10)
  if(topics1==3 and topics2=="2"):
    console.print("[green]Treatments include diet, exercise, medication, and insulin therapy.[/green]")
    sleep(10)
  if(topics1==4 and topics2=="1"):
    console.print("[red]Early treatment with medications like tPA (clot buster) can minimize brain damage. Other treatments focus on limiting complications and preventing additional strokes.[/red]")
    sleep(10)
  if(topics1==4 and topics2=="2"):
    console.print("[pink]Emergency treatment is needed for cerebral hemorrhage. It usually involves medications and close monitoring in an intensive care unit. In rare cases, surgery may be needed to relieve pressure around the brain.[/pink]")
    sleep(10)
  if(topics1==4 and topics2=="3"):
    console.print("[purple]Emergency treatment is needed for cerebral hemorrhage. It usually involves medications and close monitoring in an intensive care unit. In rare cases, surgery may be needed to relieve pressure around the brain.[/purple]")
    sleep(10)



