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


ggplot(agedata.csv, aes(x = Country, y = `Mean total cholesterol (mmol/L)`, fill = `Age group`)) + 
  stat_summary(fun = "mean", geom = "bar", position = "dodge") +
  labs(title = "Mean Cholesterol Levels by Country and Age Group",
       x = "Country", y = "Mean Cholesterol Levels") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        plot.margin = margin(1.5, 1.5, 1.5, 1, "cm"),
        plot.title = element_text(hjust = 0.4))








