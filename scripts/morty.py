#!/usr/bin/env python
def part1by1(n):
  n&= 0x0000ffff
  n = (n | (n << 8)) & 0x00FF00FF
  n = (n | (n << 4)) & 0x0F0F0F0F
  n = (n | (n << 2)) & 0x33333333
  n = (n | (n << 1)) & 0x55555555
  return n


def unpart1by1(n):
  n&= 0x55555555
  n = (n ^ (n >> 1)) & 0x33333333
  n = (n ^ (n >> 2)) & 0x0f0f0f0f
  n = (n ^ (n >> 4)) & 0x00ff00ff
  n = (n ^ (n >> 8)) & 0x0000ffff
  return n


def morton2(x, y):
  return part1by1(x) | (part1by1(y) << 1)


def demorton2(n):
  return unpart1by1(n), unpart1by1(n >> 1)


def part1by2(n):
  n&= 0x000003ff
  n = (n ^ (n << 16)) & 0xff0000ff
  n = (n ^ (n <<  8)) & 0x0300f00f
  n = (n ^ (n <<  4)) & 0x030c30c3
  n = (n ^ (n <<  2)) & 0x09249249
  return n


def unpart1by2(n):
  n&= 0x09249249
  n = (n ^ (n >>  2)) & 0x030c30c3
  n = (n ^ (n >>  4)) & 0x0300f00f
  n = (n ^ (n >>  8)) & 0xff0000ff
  n = (n ^ (n >> 16)) & 0x000003ff
  return n


def morton3(x, y, z):
  return part1by2(x) | (part1by2(y) << 1) | (part1by2(z) << 2)


def demorton3(n):
  return unpart1by2(n), unpart1by2(n >> 1), unpart1by2(n >> 2)


def morton2_bis(x, y):
  x = bin(x)[2:]
  lx = len(x)
  y = bin(y)[2:]
  ly = len(y)
  L = max(lx, ly)
  m = 0
  for j in xrange(1, L+1):
    # note: ith bit of x requires x[lx - i] since our bin numbers are big endian
    xi = int(x[lx-j]) if j-1 < lx else 0
    yi = int(y[ly-j]) if j-1 < ly else 0
    m += 2**(2*j)*xi + 2**(2*j+1)*yi
  return m/4

def morton3_with_levels(x, y, z, l, max_l):
  lev_rescale = 2**(max_l-l)
  x_scaled = x*lev_rescale
  y_scaled = y*lev_rescale
  z_scaled = z*lev_rescale
  return morton3(x_scaled, y_scaled, z_scaled)

if __name__ == '__main__':
  print(morton3(3, 2, 4))
  # points from the Figure 8.7 from
  # http://flash.uchicago.edu/site/flashcode/user_support/flash_ug_devel/node58.html
  # coordinates logic follows the figure from
  # https://homes.esat.kuleuven.be/~keppens/amrstructure.html
  point_list = [ (0, 0,  0, 1, 3), (1, 0,  0, 1, 3), (0, 1,  0, 1, 3), (1, 1,  0, 1, 3),
                 (2, 0,  0, 1, 3), (3, 0,  0, 1, 3), (2, 1,  0, 1, 3), (3, 1,  0, 1, 3),
                 (0, 2,  0, 1, 3), (1, 2,  0, 1, 3), (0, 3,  0, 1, 3), (2, 6,  0, 2, 3),
                 (3, 6,  0, 2, 3), (2, 7,  0, 2, 3), (6, 14, 0, 3, 3), (7, 14, 0, 3, 3),
                 (6, 15, 0, 3, 3), (7, 15, 0, 3, 3), (2, 2,  0, 1, 3), (3, 2,  0, 1, 3),
                 (4, 6,  0, 2, 3), (5, 6,  0, 2, 3), (4, 7,  0, 2, 3), (5, 7,  0, 2, 3),
                 (6, 6,  0, 2, 3), (7, 6,  0, 2, 3), (6, 7,  0, 2, 3), (7, 7,  0, 2, 3) ]
  for point in point_list:
      print("point: "+str(point)," - morton: "+str(morton3_with_levels(*point)))
