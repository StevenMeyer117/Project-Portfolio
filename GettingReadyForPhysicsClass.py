# You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions
# that will help them calculate some fundamental physical properties.

# Write a
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Function converts degree F to degree C
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
c_temp = f_to_c(100)
print(c_temp)

# Function converts degree C to degree F
def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp
f_temp =c_to_f(0)
print(f_temp)

# Function get force, returns mass multiplied by acceleration
def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Function get energy returns mass multiplied by constant squared
def get_energy(mass, c = 3 * 10 ** 8):
  return mass * c ** 2
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Function get work returns force
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")