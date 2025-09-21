def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    header = lines[0].strip().split(',')
    rating_idx = header.index('rating')
    votes_idx = header.index('votes')
    ratings = []
    votes = []
    for line in lines[1:]:
        parts = line.strip().split(',')
        try:
            rating = float(parts[rating_idx])
            vote = int(parts[votes_idx])
            ratings.append(rating)
            votes.append(vote)
        except:
            continue
    return ratings, votes

def mean(data):
    return sum(data) / len(data) if data else 0

def median(data):
    n = len(data)
    if n == 0:
        return 0
    data_sorted = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        return (data_sorted[mid - 1] + data_sorted[mid]) / 2
    else:
        return data_sorted[mid]

def mode(data):
    if not data:
        return None
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    return modes[0] if modes else None

def main():
    filename = 'imdb-movies-dataset.csv'
    ratings, votes = read_csv(filename)
    print('Ratings:')
    print('Mean:', mean(ratings))
    print('Median:', median(ratings))
    print('Mode:', mode(ratings))
    print('\nVotes:')
    print('Mean:', mean(votes))
    print('Median:', median(votes))
    print('Mode:', mode(votes))

if __name__ == '__main__':
    main()