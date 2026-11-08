


# score = 0
# offices = ["Bengaluru", "Mumbai", "Dubai"]



# for office in offices:
#     if "bengaluru" in office.lower() or "mumbai" in office.lower():
#         score += 20
#         break

# print(score)

score = 0
offices = ["Bengaluru", "Mumbai", "Dubai"]

has_india = False
for office in offices:
    if "mumbai" in office.lower() or "bengaluru" in office.lower():
        has_india = True
        break


if has_india:
    score += 20

print(score)