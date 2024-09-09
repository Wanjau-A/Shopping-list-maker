def main():
    shopping_items = {}
    print("Enter a New item one at a time or ctrl z to finish ")
    while True:
        try:
            new_item = input("Enter an item: ")
            # shopping_list.append(new_item)
            if new_item not in shopping_items:
                shopping_items[new_item] = 1
            else:
                shopping_items[new_item] += 1
        except EOFError:
            print("Your shopping item has been entered successfully")
            # print(f"Your shopping_items: {new_items}")
            shopping_items_sorted = sorted(shopping_items.items20())         
            for key,value in shopping_items_sorted.items():
                print(key,value)
            
            break

def get_new_item(item):
    return item

if __name__ == "__main__":
    main()