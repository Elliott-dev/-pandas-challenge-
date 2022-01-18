#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[3]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[7]:


total_player_count = len(purchase_data["SN"].unique())
total_player_count

# Creating a Summary DataFrame for the total number of players 
player_count_table = pd.DataFrame({"Total Players": [player_count]})
player_count_table


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[18]:


# Number of items that are unique
unique_items_count = len(purchase_data["Item ID"].unique())

# Average of the Purchase Price
avg_purchase_price = purchase_data["Price"].mean()

# Total Number of Purchases
total_purchases = len(purchase_data["Purchase ID"].unique())


# In[19]:


# Total Revenue
total_revenue = purchase_data["Price"].sum()

# Creating a Summary DataFrame of the purchase analysis
purchasing_analysis_table = pd.DataFrame([{
    "Number of Unique Items": unique_items_count, 
    "Average Price": avg_purchase_price,
    "Number of Purchases": total_purchases,
    "Total Revenue": total_revenue,
}], columns=["Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"])

purchasing_analysis_table["Average Price"] = purchasing_analysis_table["Average Price"].map("${0:.2f}".format)
purchasing_analysis_table["Total Revenue"] = purchasing_analysis_table["Total Revenue"].map("${0:,.2f}".format)
purchasing_analysis_table


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[20]:


male_players = purchase_data.loc[purchase_data["Gender"] == "Male"]
male_count = len(male_players["SN"].unique())
male_percent = "{:.2f}%".format(male_count / player_count * 100)

# Count and the Percentage of Female Players
female_players = purchase_data.loc[purchase_data["Gender"] == "Female"]
female_count = len(female_players["SN"].unique())
female_percent = "{:.2f}%".format(female_count / player_count * 100)

# Count and the  Percentage of Non-Disclosed
other_players = purchase_data.loc[purchase_data["Gender"] == "Other / Non-Disclosed"]
other_count = len(other_players["SN"].unique())
other_percent = "{:.2f}%".format(other_count / player_count * 100)


# In[21]:


# Creating a Summary DataFrame of the gender demographics
gender_demographics_table = pd.DataFrame([{
    "Gender": "Male", "Total Count": male_count, 
    "Percentage of Players": male_percent}, 
    {"Gender": "Female", "Total Count": female_count, 
     "Percentage of Players": female_percent}, 
    {"Gender": "Other / Non-Disclosed", "Total Count": other_count, 
     "Percentage of Players": other_percent
    }], columns=["Gender", "Total Count", "Percentage of Players"])

gender_demographics_table = gender_demographics_table.set_index("Gender")
gender_demographics_table.index.name = None
gender_demographics_table


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[42]:


male_purchase_data = purchase_data.loc[purchase_data["Gender"] == "Male", :]
male_purchase_count = len(male_purchase_data)
avg_male_purchase_price = purchase_data.loc[purchase_data["Gender"] == "Male", ["Price"]].mean()
total_male_purchase_value = purchase_data.loc[purchase_data["Gender"] == "Male", ["Price"]].sum()


# In[43]:


female_purchase_data = purchase_data.loc[purchase_data["Gender"] == "Female", :]
female_purchase_count = len(female_purchase_data)
avg_female_purchase_price = purchase_data.loc[purchase_data["Gender"] == "Female", ["Price"]].mean()
total_female_purchase_value = purchase_data.loc[purchase_data["Gender"] == "Female", ["Price"]].sum()
other_purchase_data = purchase_data.loc[purchase_data["Gender"] == "Other / Non-Disclosed", :]
other_purchase_count = len(other_purchase_data)
avg_other_purchase_price = purchase_data.loc[purchase_data["Gender"] == "Other / Non-Disclosed", ["Price"]].mean()
total_other_purchase_value = purchase_data.loc[purchase_data["Gender"] == "Other / Non-Disclosed", ["Price"]].sum()


# In[44]:


# Average Purchase Total per Person by Gender
avg_male_purchase_total_person = total_male_purchase_value / male_count
avg_female_purchase_total_person = total_female_purchase_value / female_count
avg_other_purchase_total_person = total_other_purchase_value / other_count


# In[45]:


# Creating a Summary DataFrame of the gender purchasing analysis
gender_purchasing_analysis_table = pd.DataFrame([{
    "Gender": "Female", "Purchase Count": female_purchase_count, 
    "Average Purchase Price": "${:.2f}".format(avg_female_purchase_price[0]), 
    "Total Purchase Value": "${:.2f}".format(total_female_purchase_value[0]), 
    "Avg Total Purchase per Person": "${:.2f}".format(avg_female_purchase_total_person[0])}, 
    {"Gender": "Male", "Purchase Count": male_purchase_count, 
     "Average Purchase Price": "${:.2f}".format(avg_male_purchase_price[0]), 
     "Total Purchase Value": "${:,.2f}".format(total_male_purchase_value[0]), 
     "Avg Total Purchase per Person": "${:.2f}".format(avg_male_purchase_total_person[0])}, 
    {"Gender": "Other / Non-Disclosed", "Purchase Count": other_purchase_count, 
     "Average Purchase Price": "${:.2f}".format(avg_other_purchase_price[0]), 
     "Total Purchase Value": "${:.2f}".format(total_other_purchase_value[0]), 
     "Avg Total Purchase per Person": "${:.2f}".format(avg_other_purchase_total_person[0])
    }], columns=["Gender", "Purchase Count", "Average Purchase Price", "Total Purchase Value", "Avg Total Purchase per Person"])

gender_purchasing_analysis_table = gender_purchasing_analysis_table.set_index("Gender")
gender_purchasing_analysis_table.index.name = None
gender_purchasing_analysis_table


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[28]:


# Establish the Bins for Ages & Create Corresponding Names For Bins
age_bins = [0, 9, 14, 19, 24, 29, 34, 39, 46]
groups_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# Place Data Series Into New Column Inside DataFrame
purchase_data["Age Group"] = pd.cut(purchase_data["Age"], bins=age_bins, labels=groups_names)
purchase_data

# Create a GroupBy Object Based Upon "Age Group"
age_group = purchase_data.groupby("Age Group")

# Count Total Players by Age Category
total_count_age = age_group["SN"].nunique()


# In[29]:


# Calculate the Percentages by Age Category 
percentage_by_age = round(total_count_age / player_count * 100,2)

# Create Summary DataFrame of the age demographics table
age_demographics_table = pd.DataFrame({
   "Total Count": total_count_age, 
   "Percentage of Players": percentage_by_age
})

age_demographics_table["Percentage of Players"] = age_demographics_table["Percentage of Players"].map("{0:,.2f}%".format)
age_demographics_table.index.name = None
age_demographics_table


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[40]:


# Establish Bins for Ages & Create Corresponding Names For The Bins
bins = [0, 9, 14, 19, 24, 29, 34, 39, 46]
groups_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# Place Data Series Into New Column Inside DataFrame
purchase_data["Age Group"] = pd.cut(purchase_data["Age"], bins=age_bins, labels=groups_names)

# Calculate "Purchase Count"
age_purchase_count = age_group["SN"].count()

# Calculate "Average Purchase Price"
avg_age_purchase_price = round(age_group["Price"].mean(),2)

# Calculate "Total Purchase Value"
total_age_purchase_value = round(age_group["Price"].sum(),2)


# In[41]:


# Calculate "Avg Total Purchase per Person"
avg_total_age_purchase_person = round(total_age_purchase_value / total_count_age,2)

# Create Summary DataFrame of age purchasing analysis 
age_purchasing_analysis_table = pd.DataFrame({
    "Purchase Count": age_purchase_count, 
    "Average Purchase Price": avg_age_purchase_price,
    "Total Purchase Value": total_age_purchase_value,
    "Avg Total Purchase per Person": avg_total_age_purchase_person
})

age_purchasing_analysis_table["Average Purchase Price"] = age_purchasing_analysis_table["Average Purchase Price"].map("${0:,.2f}".format)
age_purchasing_analysis_table["Total Purchase Value"] = age_purchasing_analysis_table["Total Purchase Value"].map("${0:,.2f}".format)
age_purchasing_analysis_table["Avg Total Purchase per Person"] = age_purchasing_analysis_table["Avg Total Purchase per Person"].map("${0:,.2f}".format)
age_purchasing_analysis_table


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[33]:


# Identify the Top 5 Spenders in the Game by Total Purchase Value & GroupBy "SN"
top_spenders = purchase_data.groupby("SN")

# Calculate "Purchase Count"
spender_purchase_count = top_spenders["Purchase ID"].count()

# Calculate "Average Purchase Price"
average_spender_purchase_price = round(top_spenders["Price"].mean(),2)

# Calculate "Total Purchase Value"
total_spender_purchase_value = top_spenders["Price"].sum()

# Create Summary DataFrame of top spenders table
top_spenders_table = pd.DataFrame({ 
    "Purchase Count": spender_purchase_count,
    "Average Purchase Price": average_spender_purchase_price,
    "Total Purchase Value": total_spender_purchase_value
})

sort_top_spenders = top_spenders_table.sort_values(["Total Purchase Value"], ascending=False).head()
sort_top_spenders["Average Purchase Price"] = sort_top_spenders["Average Purchase Price"].astype(float).map("${:,.2f}".format)
sort_top_spenders["Total Purchase Value"] = sort_top_spenders["Total Purchase Value"].astype(float).map("${:,.2f}".format)
sort_top_spenders


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[34]:


# Identify the 5 Most Popular Items by Creating New DataFrame
popular_items_list = purchase_data[["Item ID", "Item Name", "Price"]]

# GroupBy "Item ID" & "Item Name"
popular_items = popular_items_list.groupby(["Item ID","Item Name"])

# Calculate "Purchase Count"
item_purchase_count = popular_items["Price"].count()

# Calculate "Item Price"
item_price = popular_items["Price"].sum()

# Calculate "Total Purchase Value" 
item_purchase_value = item_price / item_purchase_count

# Create Summary DataFrame of the most popular items 
most_popular_items = pd.DataFrame({
   "Purchase Count": item_purchase_count, 
   "Item Price": item_purchase_value,
   "Total Purchase Value": item_price
})

popular_items_formatted = most_popular_items.sort_values(["Purchase Count"], ascending=False).head()
popular_items_formatted["Item Price"] = popular_items_formatted["Item Price"].astype(float).map("${:,.2f}".format)
popular_items_formatted["Total Purchase Value"] = popular_items_formatted["Total Purchase Value"].astype(float).map("${:,.2f}".format)
popular_items_formatted


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[35]:


popular_items_formatted = most_popular_items.sort_values(["Total Purchase Value"], ascending=False).head()
popular_items_formatted["Item Price"] = popular_items_formatted["Item Price"].astype(float).map("${:,.2f}".format)
popular_items_formatted["Total Purchase Value"] = popular_items_formatted["Total Purchase Value"].astype(float).map("${:,.2f}".format)
popular_items_formatted


# In[47]:


print("A great deal of players, approximately 75%, are between the ages of 15 and 29 years old and on average they spend $2.99.")
print("With a total purchase value of $13.32 the top 5 spenders spend on average $3.45 per purchase.")
print("Nirvana, Fiery Glass Crusader, and Othbreaker(Last Hope of the Breaking Storm) are 3 of the most popular items and they are also the most profitable.")


# In[ ]:




