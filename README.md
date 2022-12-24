[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9628777&assignment_repo_type=AssignmentRepo)

<h1 align="center">DiFA</h1>

<h3 align="center">Your personal Digital Financial Advisory for Mutual Funds</h3>

<p align="center">
  <img src="https://media.discordapp.net/attachments/1053904949265829930/1054578020792414228/logodifa.png?width=636&height=636"></img>
</p>
Repository contributors:

[Anggara Sustina](https://www.linkedin.com/in/anggara-sutisna/), [Muhammad Afif Alvan](https://www.linkedin.com/in/afif-alvan/), [Muhamad Natual Hisak](https://www.linkedin.com/in/natual-hisak-13116719a/), [Muhammad Julizar](https://www.linkedin.com/in/muhammadjulizar/), [Nadia Oktiarsy](https://www.linkedin.com/in/nadiaoktiarsy/), and [Sri Wahyuni](https://www.linkedin.com/in/sri-wahyuni-/)

---
### General Disclaimer
This repository contains Digital Financial Advisory (DiFA) models trained from scratch to give the user risk profiling and to suggest the best investment they can do right away! The following list provides an overview of all currently available models.

---
## Project's Background
What is happening with Indonesia's financial condition?

The pressures of rising prices and tightening external finance post COVID-19 is not only an international problem, Indonesia is also affected by this. Based on World Bank, there are at least three pillars to strengthen Indonesia's Economy and Financial Sector:
- Increase demand and supply of finance by **increasing access to and usage of financial services**, broadening and improving the quality of financial market products and mobilizing long-term savings.
- Improve allocation of resources through the financial sector by **promoting competition in the banking sector, strengthening the insolvency framework, and protecting consumers**
- **Strengthen the capacity of the financial system** to withstand financial and non-financial shocks by strengthening the effectiveness of financial sector oversight, strengthening crisis preparedness and resolution framework, and promoting climate and natural disaster related risk management.

This project is created to help people in Indonesia to understand more about banking and investment. By creating Digital Financial Advisory (DiFA), DiFA models have a main goal to give the best solution for investors to know directly their *Risk Profiling* of Mutual Funds. Another features that are available from DiFA is also to recommend investors which Mutual Funds and Stocks with the best bid for that day based on investors' profile.

---
## 1. Investors Profiling
Through DiFA, this is to assess users which **Risk Profile** based on users charaacteristics and personality. New users or investors will be asked to fill some questionnaires (10 questions) which are related to:
- Investment Time Horizon
- Investment Knowlegde
- Risk Capacity, and 
- Risk Attitude

After new users/investors submit the questions, they will be directly classified as one of three profiles: \

| Risk Profiles        | Description           |
| ------------- |-------------|
| *High Risk Investor* | Investors tolerance for risk, portfolio volatility and investment losses is high or very high. Investors are willing to tolerate potentially significant and sustained price fluctuations and large losses of capital. Investors have extensive investment knowledge. Investors have no income requirements from your investments and have a long investment time horizon. |
| *Medium Risk Investor*| Investors have a moderate tolerance for risk and loss of capital. Investors are willing to tolerate some fluctuations in your investment returns and moderate losses of capital. Investors have at least a medium term investment time horizon. The objective of investors portfolio will be to provide a combination of income and long term capital growth and therefore the portfolio will include at least 40% in fixed income investments. |
| *Low Risk Investor* | Investors have a low tolerance for risk and potential loss of capital or a short investment time horizon. Investors are willing to accept some short term fluctuations and small losses in your investment portfolio in exchange for modest returns. The primary objective of your investment portfolio will be to provide income by investing primarily in funds that invest in fixed-income securities. While capital appreciation is not a priority, a small portion of the portfolio may be invested in equity funds to provide the potential for some growth to offset the impact of inflation.|

## 2. Mutual Funds Recommendation
After investors know their risk profile, they will directly be informed the most recommended Mutual Funds. In this model, we have 10 Mutual Funds for each Risk Profile. The top 3 Mutual Funds that have the best prediction of NAV (Net Asset Value) will be shown especially for **Low** and **Medium Risk Profile**. Meanwhile, for **High Risk Profile**, investors will get further information not only NAV (Net Asset Value) but also Stocks that are going to increase.

## 3. How to use DiFA

[DiFA Demo Program](https://youtu.be/mzxee4i6kz0)

<p align="center">
  <img src="https://github.com/H8-Assignments-Bay/p2---final-project-ftds-016-rmt-group-002/blob/main/Studio_Project.gif"></img>
</p>

[DiFA Deployment](https://huggingface.co/spaces/NatualHisak/DiFA)


### Shout-Outs
- [World Bank](https://www.worldbank.org/en/country/indonesia/publication/indonesia-economic-prospects-iep-june-2022-financial-deepening-for-stronger-growth-and-sustainable-recovery)
- [Sample Investor Questionnaire](https://mfda.ca/ipq/)
- [Vanguard](https://investor.vanguard.com/home)
- [Bareksa](https://www.bareksa.com/)
- [Bibit.com](https://bibit.id/)
