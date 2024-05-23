def f(x):
  return x**3 - x - 1

def f_prime(x):
  return 3 * x**2 - 1

def newton_raphson(x0, max_iter=21,tolerance=1e-7):
  x = x0
  results = [x]
  for _ in range(max_iter):
      h = f(x) / f_prime(x)
      if abs(h) < tolerance:
          break
      x = x - h

      results.append(x)

  return results

x0 = 0
iterations = newton_raphson(x0, max_iter=20)

# Ekrana yazdırma
for i in range(len(iterations)):
  print(f"x_{i} = {iterations[i]}")
