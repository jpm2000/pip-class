def ordenes(data, cliente):
  result = list(filter(lambda cli : cli['customerName'] == cliente, data))
  return result