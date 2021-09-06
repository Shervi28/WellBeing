#shreyansh
from time import sleep
from os import system, name 
from rich.console import Console
from pyfiglet import Figlet, figlet_format
from rich.table import Table
console = Console()

def main6():
    console.print("Pills for...: ")
    console.print("\n")
    console.print("1.Pills for Headaches")
    console.print("\n")
    console.print("2.Pills for pains")
    console.print("\n")
    console.print("3.Pills for Wieght loss")
    console.print("\n")
    console.print("4.Pills for Memory")
    console.print("\n")
    console.print("5.Pills for Sleeping")
    Pills_For = input("Enter a number:")
    if Pills_For=="1":
        table = Table(title="For ")
        table.add_column("Generic Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Brand Name", style="magenta")
        table.add_column("Use", justify="right", style="green")
        table.add_column("Precautions", justify="right", style="red")
        table.add_column("Possible Side Effects", justify="right", style="blue")

        table.add_row("Acetaminophen", "Panadol, Tylenol", "Pain Relief Headache treatment", "", "Few side effects if taken as directed, although they may include: changes in blood counts and liver damage")
        table.add_row("Aspirin", "Bayer, Bufferin", "Pain relief Headache treatment","Do not use in children younger than age 19 years due to the potential for Reye's syndrome (a life-threatening neurological condition)","Heartburn, gastrointestinal bleeding, bronchospasm or constriction that causes narrowing of the airways, anaphylaxis (life-threatening allergic reaction), ulcers")
        table.add_row("Fenoprofen", "Nalfon", "Prevention of tension headaches; migraines; hormone headaches", "none", "Nausea, diarrhea, indigestion, dizziness, drowsiness")
        table.add_row("Flurbiprofen", "Ocufen", "Prevention of tension headaches; migraines. Treatment of tension headache; migraines", "none", "Gastrointestinal upset, drowsiness, dizziness, vision problems, ulcers")


        
        console.print(table)
    if Pills_For=="2":
        console.print("Acetaminophen")
        console.print("Nonsteroidal Anti-Inflammatory Drugs (NSAIDs)")
        console.print("Antidepressants")
        console.print("Anticonvulsants")
    if Pills_For=="3":
        pass