library(rstatix)
library(tidyverse)
library(ggplot2)
library(dplyr)
#Load in data
agedata.csv = read_csv("agespec.csv")
head(agedata.csv)
summary(agedata.csv)

agedata.csv = agedata.csv %>%
  mutate(Country = ifelse(Country == "United States of America", "United States", Country))

agedata.csv = agedata.csv %>%
  filter(Year >= 2000)

countries_to_keep <- c("United States", "Mexico", "Vietnam", "United Kingdom", "Canada", "China")

agedata.csv = agedata.csv %>%
  filter(Country %in% countries_to_keep)

ggplot(agedata.csv, aes(x = Country, fill = `Age group`)) + 
  geom_bar(position = "dodge") +
  labs(title = "Cholesterol Levels by Country and Age Group", x = "Country", y = "Cholesterol Levels")
