  import pandas as pd
  import matplotlib.pyplot as plt
  
  # Assuming gamestop_data and revenue_data are prepared
  plt.figure(figsize=(10, 5))
  plt.plot(gamestop_data['Date'], gamestop_data['Close'], label='Stock Price', color='green')
  plt.title('GameStop Stock Price over Time')
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.legend()
  plt.show()
  