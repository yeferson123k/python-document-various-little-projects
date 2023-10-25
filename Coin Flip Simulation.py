import random

def coin_flip_simulation(num_flips):
    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        coin_result = random.randint(0, 1)

        if coin_result == 0:
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count

def main():
    num_flips = int(input("Enter the number of coin flips: "))

    heads_count, tails_count = coin_flip_simulation(num_flips)

    print(f"Number of heads: {heads_count}")
    print(f"Number of Tails: {tails_count}")

if __name__ =="__main__":
    main()
