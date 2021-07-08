

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



# Binance API Price Data Interface

Using Binance's API this script obtains the historical price data of a specified asset, given the time range and time frame of interest as inputs.
This price data is then parsed in to a dataframe ready for use in backtesting trading strategies or simply data visualisation.






### Real-World Use-Cases


💰 Attain historical price data for a wide range of assets on Binance

🏦 Data source for backtesting trading strategies





### Development-Goals


🧾 Further develop knowledge of Matplotlib and Pandas dataframes

🤖 Learn how to interact with Binance's API and understand it's limitations

☑️ Develop customisable data source for use in trading strategy backtesting




## Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Requests](https://pypi.org/project/requests/)
* [Matplotlib](https://matplotlib.org/)



<!-- GETTING STARTED -->
## Getting Started

Example function call: 

  ```py
   get_binance_data('ETHUSDT','1h', dt.datetime(2020,1,1), dt.datetime(2020,2,1))
  ```
   
This call would return a dataframe containing the price data for the Ethereum / USD Tether pair on Binance between the 1st of January 2020 and the 1st of February 2020.
  
  

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Twitter - [@TraderTDF](https://twitter.com/TraderTDF)

LinkedIn - [https://www.linkedin.com/in/RAMWatson/](https://www.linkedin.com/in/RAMWatson/)

Project Link: [https://github.com/Elisik/Binance-API-Price-Data-Interface](https://github.com/Elisik/Binance-API-Price-Data-Interface)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/RAMWatson/


