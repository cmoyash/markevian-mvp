domains = ["facebook.com", "abcagency.com", "instagram.in", "webfx.io"]


# for d in domains:
#     print("facebook" in d)


# results = [False, False, True]
# results2 = [False, False, False]
# results3 = [True, True, True]
# results4 = [False, True, True]




# p = "facebook.com"
# bad_list = ["facebook", "instagram", "linkedin"]

# checks = []
# for bad in bad_list:
#     checks.append(bad in p)





p = "abcagency.com"
bad_list = ["facebook", "instagram", "linkedin"]


result  = any(bad in p for bad in bad_list)
print(result)