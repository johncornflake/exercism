def slices(series, length):
    if length > len(series) or length < 1 or len(series) == 0:
        raise ValueError('Invalid length provided')
    else:
        return [series[i:i+length] for i in range(len(series)+1 - length)]
