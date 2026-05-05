import json
def main():
  ledger = []
  print("My Personal Finance Tracker")

  while True:
    print("\n1. Add Transaction")
    print("2. View Summary")
    print("3. Save and Exit")

    choice = input("Select an option (1-3): ")
    if choice == '1':
      item = input("What did you buy?")
      amount = float(input("How much?"))
      category = input("Category (Health,Food,Education):")
      ledger.append({"item":item, "amount":amount, "category":category})
      print("Transaction Added!")
    elif choice == '2':
      total = sum(item['amount']for item in ledger)
      print("\nSummary")
      for entry in ledger:
        print(f"{entry['category']}:{entry['item']} - {entry['amount']}")
      print(f"Total Spending:{total}")
    
    elif choice == '3':
      with open('my_ledger.json','w') as f:
        json.dump(ledger,f)
    print("Data SAved.Goodbye!")
    break
if __name__ == "__main__":
  main()
