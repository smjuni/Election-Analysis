
# counties = ["Arapahoe", "Denver", "Jefferson"]

# print(counties[2])

# if counties[1] == "Denver":
#         print(counties[1])

# if counties[1] != "Jefferson"
#        print(counties[2])

# if "El Paso" in counties:
#         print("El Paso is in the list of counties")
# else:
#         print("El Paso is not in the list of counties")

# if "Arapahoe" in counties and "El Paso" not in counties:
#         print("Only Arapahoe is in the list of counties")
# else:
#         print("Arapahoe is in the list of counties and El Paso is not in the list of counties")


# for county in counties:
#         print(county)

# for i in range(len(counties)):
#         print(counties[i])


# counties_dict= {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict.keys():
#     print(county)    
# print(counties_dict["Arapahoe"])

# for voters in counties_dict.values():
#         print(voters)

# for county, voters in counties_dict.items():
#         print(county, voters)

#Skill Drill 3.2.10
# counties_dict= {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
        # print(county + " county has " + str(voters) + " registered voters.")
#        print(f"{county} county has {voters:,} registered voters.")
#         Incorrect. print(f'{counties_dict["county"]}, "County has" {counties_dict["voters"]}, "registered voters."')
#        Incorrect  # print(f'{counties_dict.get[county]} "county has" {counties_dict.get[voters]} "registered voters."')
        #incorrect  print(f'"(county) "County has" (voters) "registered voters.""')


# candidate_votes = int(input("How many votes did you get in the election?"))
# total_votes = int(input("what is the total votes in the election?"))
# #percentage_votes = (my_votes/total_votes)*100
# #print("I received " + str(percentage_votes)+ "% of the total votes.")
# #print(f"I received {my_votes/total_votes *100}% of the total votes.")
# message_to_candidate = (
#         f"You received {candidate_votes:,} number of votes. "
#         f"The total number of votes in the election was {total_votes:,}. "
#         f"You received {candidate_votes/total_votes * 100:.2f}% of the total votes.")
# print(message_to_candidate)

# voting_data = [{"county":"Arapahoe", "registered_voters":422829, "county":"Denver", 
# "registered_voters": 463353, "county":"Jefferson", "registered_voters":432438}]
# For county, registered_voters in voting_data.items():
# print(f"{voting_data'county'} county has {voting_data'registered_voters':,} registered voters.")