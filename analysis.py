import numpy as np 
data = np.genfromtxt('supermart_sales.csv' , delimiter=',' , skip_header=1,dtype=str)


unit_sold = data[:,4].astype(int)
unit_price = data[:,5].astype(int)
discount= data[:,6].astype(int)
customer = data[:,7].astype(float)
region = data[:,8].astype(str)
category = data[:,3].astype(str)
product = data[:,2].astype(str)
month = data[:,1].astype(str)
order_id = data[:,0].astype(int)

#Q1. Find the total units sold in all orders.

total_sold = np.sum(unit_sold)
# print(total_sold)

#Q2. Find the average price of all products.
avg_pro = np.average(unit_price)
# print(avg_pro)

#Q3 Find the highest units sold in any order.

highest_unit = np.max(unit_sold)
# print(highest_unit)

#Q4. Find the lowest customer rating.
lowest_cus = np.min(customer)
# print(lowest_cus)

#Q5. Find the index number of the order with the highest units sold.
index_max = np.argmax(unit_sold)
# print(index_max)

#Q6. Arrange all customer ratings from smallest to largest.
customer_rating = np.sort(customer)
# print(customer_rating)

#Q7. Count how many different products are present.
diff_pro = np.unique(product)
# print(diff_pro)

#Q8. Find total revenue for row where discount is 0 .

revenue = 0 
for i in range(len(discount)):
    if discount[i]==0:
        revenue += unit_price[i]*unit_sold[i]

# print(revenue)

#Q8. Finf total revenue if dicount is not given 
revenue = unit_sold*unit_price
# print(sum(revenue))

#Q9. Round all revenue values to the nearest integer.

nerest = np.round(revenue)
# print(nerest)


# Q10. Find the difference between the highest and lowest product price.

diff = np.max(unit_price)-np.min(unit_price)
# print(diff)

# Q11. Show all orders where units sold is more than 100.

# print(order_id[unit_sold>100])

# Q12.  Count how many orders received a discount

count = order_id[discount>0]
# print(len(count))
# Q13. Find the average customer rating for Electronics products.

average_customer_rating = np.average(customer[category=='Electronics'])
# print(average_customer_rating)

# Q14. Show product names where customer rating is less than 4.

product_name = product[customer<4]
# print(product_name)


# Q15.  revenue after discount for every order and show the top 3 highest revenues.

revenue_after_discount = unit_price * unit_sold * (1 - discount/100)
t = np.sort(revenue_after_discount)
# print(t[-3:])

# Q16. Find the percentage of orders having rating 4.5 or above.

count = order_id[customer>=4.5]
# print(count)
percentage = (len(count)/len(customer))*100

# print(np.round(percentage))

# Q17. Find the region that sold the most units.

reg = region[unit_sold == np.max(unit_sold)]
# print(reg)

# Q18. Find the month with the highest average customer rating.

unique_month = np.unique(month)
average_customer_rating = []
for m in month:
    avg = np.mean(customer[month==m])
    average_customer_rating.append(avg)

highest_avg = np.max(average_customer_rating)
# print(np.round(highest_avg))


# Q19. Create a new column:

# "high" if revenue > 500000
# "low" otherwise

new = np.where(revenue>50000,'High' , 'Low')
data = np.column_stack((data,new))
# print(data)

# Q20. Find how total units sold changed from one month to the next month.
total_add=[]
for m in unique_month:
    add = np.sum(unit_sold[month==m])
    total_add.append(add)

chnaged = np.diff(total_add)


# print(chnaged)

# Q21. Find the product with the highest average customer rating.

unique_pro = np.unique(product)
hacr = []
for p in unique_pro:
    avg = np.mean(customer[product==p])
    hacr.append(avg)

# print(np.max((hacr)))

# Q22. Show orders where:

# Units sold > 50
# Discount > 5

# # Also count those orders./


show = (unit_sold>50) & (discount>5)
# print(data[show])
# print(len(show))

# Q23. Find the total money lost because of discounts.


money_lost = np.abs(revenue_after_discount -revenue)
# print(np.sum(money_lost))

# Q24. Find which category earned the highest share of total revenue.

unique_cat = np.unique(category)
high_rev = []
for r in unique_cat:
    add = np.sum(revenue[category==r])
    high_rev.append(add)

idx = np.argmax(high_rev)
# print(unique_cat[idx])
# print(high_rev[idx])

# Q25. Find the top 3 months with the highest revenue and rank them:

err = []
for m in unique_month:
    jodo = np.sum(revenue[month==m])
    err.append(jodo)


idx = np.argsort(err)[::-1]
print(unique_month[idx[:3]])
print(np.array(err)[idx[:3]])


