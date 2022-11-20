def savings(gross_pay, tax_rate, expenses):

    takehome_pay = (int(gross_pay) * (1-float(tax_rate))) - int(expenses)

    return int(takehome_pay)
    
def material_waste(total_material, material_units, num_jobs, job_consumption):

    material_input_wasted =  str(total_material-(num_jobs*job_consumption)) + str(material_units)
    
    return material_input_wasted
  
def interest(principal, rate, periods):
    
    interest = (int(principal * (float(rate)*periods)+principal))
    
    return interest
  
def body_mass_index(weight, height):
    a= weight/2.205
    b= int(height[0]) / 3.281
    c= int(height[1]) / 39.37

    bmi = a / (b + c)**2

    return bmi
