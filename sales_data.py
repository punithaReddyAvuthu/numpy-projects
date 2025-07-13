import numpy as np

sales_data = np.array([100,150,200,175,300])
print(f"Sales data:{sales_data}")
print(f"Type: {type(sales_data)}")
print(sales_data[-1])

monthly_sales = np.array([
    [100, 150,200],
    [160, 240, 169],
    [140, 170, 220]
])

print(monthly_sales[:, :2])

print(f"monthly sales shape: {monthly_sales.shape}")
print(f"size: {monthly_sales.size}")
print(f"dimensions: {monthly_sales.shape}")
print(f"data type: {monthly_sales.dtype}")

zeros_array = np.zeros(5);
one_array = np.ones((3,4))
range_array = np.arange(0, 12, 2)
linspace_array = np.linspace(0, 1, 5)

print(f"zeros: {zeros_array}")
print(f"Range: {range_array}")
print(f"linspace: {linspace_array}")

sales = np.array([100,200,150,175,300])
high_sales = sales > 180
print(f"high sales mask: {high_sales}")

high_sales_value = sales[high_sales]
print(f"high sales values: {high_sales_value}")

premium_sales = sales[sales> 200]
print(f"Premium sales: {premium_sales}")

prices = np.array([10,15,20,25])
quantities = np.array([5,3,8,2])

revenue = prices * quantities
print(f"Revenue: {revenue}")

discounted = prices * quantities
print(f"Revenue: {revenue}")

discounted_prices = prices * 0.9
tax_included = prices * 1.1

price_difference = prices - np.mean(prices)
print(f"discounted : {discounted_prices}")
print(f"discounted : {discounted_prices}")

print(f"with tax: {tax_included}")


sales_matrix = np.array([
    [100, 125, 200],
    [75, 50, 25],
    [300, 240, 340]
])

discounted = sales_matrix * 0.9
print(f"discounted : {discounted}")


monthly_bonus = np.array([10, 20, 30])
total_with_bonus = sales_matrix + monthly_bonus
print(f"sales with total including bonus: {total_with_bonus}")

data = np.array([1, 4, 9, 16, 25])

sqrt_data = np.sqrt(data)
log_data = np.log(data)
exp_data = np.exp(data)

print(f"square root: (sqrt_data)")
print(f"natural log:(log_data)")

angles = np.array([0, np.pi/4, np.pi/2, np.pi/6])
sin_values = np.sin(angles)
cos_values = np.cos(angles)
tan_values = np.tan(angles)

print(f"sine values:{sin_values}")


sales_data = np.array([100,150,250,175,300])

mean_sales = np.mean(sales_data)
median_sales = np.median(sales_data)


min_sales = np.min(sales_data)
max_sales  =np.max(sales_data)


std_sales = np.std(sales_data)
var_sales = np.var(sales_data)


print(f"mean: {mean_sales:.2f}")
print(f"median:{median_sales:.2f}")
print(f"standard deviation: {std_sales:.2f}")


visitors = np.array([
    [1200, 800, 600],
    [175, 225, 250],
    [300, 280, 320],
    [250, 270, 290]
])

total_by_day = np.sum(visitors, axis=1)
total_by_source = np.sum(visitors, axis=0)
grand_total = np.sum(visitors)

avg_by_day = np.mean(visitors, axis=1)

print("total visitors each day:", total_by_day)

print("total visitors from each source:", total_by_source)
print("grand total visitors:", grand_total)
print("average visitors per day:", avg_by_day)

data = np.arange(12)
print(f"\noriginal: {data}")

matrix_3x4 = data.reshape(3, 4)
matrix_2x6 = data.reshape(2, 6)

print(f"\n3x4 matrix: \n{matrix_3x4}")
print(f"\n2x6 matrix: \n{matrix_2x6}")

transposed = matrix_3x4.T
print(f"transposed matrix: {transposed}") 

q1_sales = np.array([100, 220, 350])
q2_sales = np.array([175, 225, 250])

np.concatenate([q1_sales, q2_sales])

np.vstack([q1_sales, q2_sales])

year_data = np.array([100, 220, 350, 175, 225, 250, 430, 470, 550, 750, 897, 940])

quarters = np.split(year_data, 4)
print(f"q1: {quarters[0]}")
print(f"q2: {quarters[1]}")



quareters = np.split(year_data, [6])

np.sort(year_data)
np.argsort(year_data)

matrix = np.array([[4,2],[1,3]])

det = np.linalg.det(matrix)
print(f"Determinanat: {det}")

inverse = np.linalg.inv(matrix)
print(f"Inverse: {inverse}")

eigenvalues, enignvectors = np.linalg.eig(matrix)
print(f"Eigen values: {eigenvalues}")
print(f"Eigen vectors: {enignvectors}")

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

matrix_product = np.dot(A, B)

element_wise = A * B



    

