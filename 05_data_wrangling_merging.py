import pandas as pd
import numpy as np
import seaborn as sns
import math


#الجزء الاول
#1
titanic = sns.load_dataset('titanic')

titanic1 = titanic.isnull().sum().sort_values(ascending= False)
print(titanic1)
titanic2 = titanic1[titanic1 > 0]
print(titanic2)


#2
titanic["age_filld"] = titanic["age"].fillna(titanic["age"].mean())


#3
titanic = titanic.drop("deck", axis=1)
print(titanic)
#شلت العامود كامل عشان كمية القيم المفقودة في كبيرة جدا لدرجة ان  التعويض باي طريقة رح يعطينة نتائج خاطئة 

#4
titanic["embarked"] = titanic["embarked"].fillna(titanic["embarked"].mode()[0])
#مع اني بفضل انو امسح السطرين اسهل ههههه

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#الجزء الثاني


dublicated_data = {"costumer_id":[101,102,103,104,102], "costumer_name":["ahmed","sara","khaled","laila","sara"],
                   "age":[28,22,35,29,22],"purchase_amount":[150,200,320,120,200]}
df_dublicated_data = pd.DataFrame(dublicated_data)
print(df_dublicated_data)
print(df_dublicated_data[df_dublicated_data.duplicated()])
clean_data = df_dublicated_data.drop_duplicates(keep= "first")
print(clean_data)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------


#الجزء الثالث

fare_mean = titanic["fare"].groupby(titanic["pclass"]).mean()
print(fare_mean)
s_sex_mean = titanic.groupby('sex')["survived"].mean()
print(s_sex_mean)
sp_sex_mean = titanic.groupby(['sex','pclass'])["survived"].mean()
print(sp_sex_mean)
pasenger_num = titanic.groupby(titanic["embarked"]).count()
pasenger_num1 = titanic['embarked'].value_counts()
print(pasenger_num1)
print(pasenger_num)

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

#الجزء الرابع


customers = pd.DataFrame({

'customer_id': [1, 2, 3, 4],

'name': ['أحمد', 'سارة', 'محمد', 'ليان'],

'city': ['عمان', 'إربد', 'الزرقاء', 'عمان']

})

orders = pd.DataFrame({

'order_id': [101, 102, 103, 104, 105],

'customer_id': [1, 2, 1, 3, 5], # لاحظ العميل رقم 5 مش موجود بجدول العملاء

'amount': [150, 200, 90, 300, 60]

})

merged = pd.merge(customers["customer_id"],orders)
print(merged)
left_marged = pd.merge(customers["customer_id"],orders, how="left")
print(left_marged)
right_marged = pd.merge(customers["customer_id"],orders, how="right")
print(right_marged)
#اللي فهمتو لحد الان انو لازم الميرج يكون عن طريق عامود مشترك بين الجدولين 
#هلا من ناحية ليش اختفى العميل رقم 5 مش كتير فاهم عشان لما عملتو يمين رجع طلع 
#هل هو يعني معتبر انو الجدول اللي فوق يسار فلما حكيتلو يسار حطلي كل الid اللي بالجدول الاول 
# و العكس صحيح لما استعملت رايت 
#مش كتير متاكد 
#قصدي انو لما احددلو يمين او يسار بنزل الجدول اللي حددتو زي ما هو و بعيض بقمة nan

# Inner Merge
merged2 = pd.merge(customers, orders, on="customer_id")
print(merged2)
# Left Merge
lefted_merged = pd.merge(customers, orders, on="customer_id", how="left")
print(lefted_merged)
#right merge
righted_merged = pd.merge(customers, orders, on="customer_id", how="right")
print(righted_merged)

#جبمناي حكالي هيك احسن عشان اعرض الجدولين كاملات 
#بس مش عارف يمكن عشان باللغة العربية الاسماء و المدن حاطهم ياماكن غلط 

customers2 = pd.DataFrame({

'customer_id': [1, 2, 3, 4],

'name': ['ahmed', 'sara', 'mohammed', 'laian'],

'city': ['amman', 'erbed', 'zarqa', 'amman']

})

orders2 = pd.DataFrame({

'order_id': [101, 102, 103, 104, 105],

'customer_id': [1, 2, 1, 3, 5], # لاحظ العميل رقم 5 مش موجود بجدول العملاء

'amount': [150, 200, 90, 300, 60]

})
# Inner Merge
merged3 = pd.merge(customers2, orders2, on="customer_id")
print(merged3)
# Left Merge
lefted3_merged = pd.merge(customers2, orders2, on="customer_id", how="left")
print(lefted3_merged)
#right merge
righted3_merged = pd.merge(customers2, orders2, on="customer_id", how="right")
print(righted3_merged)

#لما حولت الاسماء من عربي لانجليزي زبط 

#outer marge
out_merged = pd.merge(customers2, orders2,on="customer_id", how="outer")
print(out_merged)

#مش عارف ليش بالاوتر ميرج خلا احمد يتكرر ورا بعض اما الرايت لا 
#قصدي الترتيب كان مختلف
#بس الاوتر بنزل الجدويلين كاملين زي ما هم و بعوض بقيم فارغة

orders3 = pd.DataFrame({

'order_id': [106, 107, 108, 109, 110],

'customer_id': [1, 4, 1, 2, 5], # لاحظ العميل رقم 5 مش موجود بجدول العملاء

'amount': [155, 210, 85, 330, 65]
})

new_orders = pd.concat([orders2, orders3], axis=0)
print(new_orders)

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


#الجزء الخامس
customers_data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 3], 
    'name': ['Ahmad', 'Sara', 'Mohammad', 'Layan', 'Omar', 'Nourhan', 'moath', 'Roa', 'Mohammad'],
    'city': ['Amman', 'Irbid', 'Zarqa', np.nan, 'Amman', np.nan, 'Aqaba', 'Irbid', 'Zarqa']
}
customers4 = pd.DataFrame(customers_data)

# 
orders_data = {
    'order_id': range(101, 116),
    'customer_id': [1, 1, 2, 3, 3, 3, 5, 5, 6, 7, 7, 7, 8, 1, 2], 
    'amount': [150, 200, 50, 120, 300, 90, 400, 60, 110, 500, 250, 100, 350, 80, 140]
}
orders4 = pd.DataFrame(orders_data)

customers4["city"] = customers4['city'].fillna(customers4['city'].mode()[0])
print(customers4)
#بفضل تكون الاكثر تكرارا عشان لما تكون الداتا اكبر بكون الاكثر تكرارا اوضح
customers4 = customers4.drop_duplicates(keep= 'first')
print(customers4)

merged4 = pd.merge(customers4,orders4, on= "customer_id", how="left")
print(merged4)

order_count = merged4["order_id"].groupby(merged4["customer_id"]).count()
df1 = pd.DataFrame(order_count)
print(df1)

sum_order = merged4["amount"].groupby(merged4["customer_id"]).sum()
df2 = pd.DataFrame(sum_order)
print(df2)

df1_2 = pd.concat([df1, df2] ,axis=1)
df3 = pd.DataFrame(df1_2)
print(df3)

df3 = df3.sort_values(by = 'amount', ascending= False)
print(df3.head(3))

#


'''order_count = merged4.groupby("customer_id").count()
print(order_count)

sum_order = merged4.groupby(merged4["customer_id"])["amount"].sum()
print(sum_order)'''#بعض المحاولات اللي مش كتير عارف اعملهم ههههه