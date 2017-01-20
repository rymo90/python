# Quotation Manuuplation
# demonstrates string methods 

# quote from IBM Chariman, Thoms Watson, in 1943
quote = "---I Think there is a  WORLD market for maybe five computers."

print("Original qoute:")
print(quote)

print("\nIn uppercase:")
print(quote.upper())

print("\nIn strip:")
print(quote.strip())


print("\nIn lowercase:")
print(quote.lower())

print("\n in swapcase:")
print(quote.swapcase())

print("\nAs a title:")
print(quote.title())

print("\nWith a minor replacement:")
print(quote.replace("five",  "millions of"))

print("\nOriginal quote is still:")
print(quote)

input("\n\npress the enter key to exit.")