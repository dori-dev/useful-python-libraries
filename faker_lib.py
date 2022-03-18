"""faker library
"""
import faker
# pip install Faker
en_faker = faker.Faker()
fa_faker = faker.Faker('fa_IR')


print('\n----- address -----')
print(en_faker.address())
print(fa_faker.address())

print('\n----- bank -----')
print(en_faker.bank_country())
print(fa_faker.bank_country())

print('\n----- city -----')
print(en_faker.city())
print(fa_faker.city())

print('\n----- color -----')
print(en_faker.color_name())
print(fa_faker.color_name())

print('\n----- country -----')
print(en_faker.country())
print(fa_faker.country())

print('\n----- email -----')
print(en_faker.email())
print(fa_faker.email())

print('\n----- file name -----')
print(en_faker.file_name())
print(fa_faker.file_name())

print('\n----- file path -----')
print(en_faker.file_path())
print(fa_faker.file_path())

print('\n----- file name -----')
print(en_faker.name())
print(fa_faker.name())

print('\n----- text -----')
print(en_faker.text())
print(fa_faker.text())

print('\n----- female first name -----')
print(en_faker.first_name_female())
print(fa_faker.first_name_female())

print('\n----- hostname -----')
print(en_faker.hostname())
print(fa_faker.hostname())

print('\n----- phone number -----')
print(en_faker.phone_number())
print(fa_faker.phone_number())

print('\n----- password -----')
print(en_faker.password())
print(fa_faker.password())

print('\n----- word -----')
print(en_faker.word())
print(fa_faker.word())
