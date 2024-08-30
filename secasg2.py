from sympy import mod_inverse
import math

#################################################scenario1########################################
p = 23
g = 5
public_key = 21  # g^x mod p
c1 = 10  # g^y mod p
c2 = 9   # (g^xy * m) mod p

# Step 1: Find the private key x such that g^x ≡ public_key mod p
x = None
for i in range(1, p):
    if pow(g, i, p) == public_key:
        x = i
        break

if x is None:
    raise ValueError("Private key x could not be found")

# Step 2: Compute g^xy mod p using c1 and x
g_xy_mod_p = pow(c1, x, p)

# Step 3: Compute the modular inverse of g^xy mod p
g_xy_inverse_mod_p = mod_inverse(g_xy_mod_p, p)

# Step 4: Recover the message m
m = (c2 * g_xy_inverse_mod_p) % p

# Print the recovered message
print("Scenario 1 m:", m)


###############################################################scenario2########################################################
# Define the parameters
p = 95768907671470685161834890931411566592455689334949078397684923142851642341551
g = (p + 1) // 2
public_key = 47884453835735342580917445465705783296227844667474539198842461571425821170776
c1 = 47884453835735342580917445465705783296227844667474539198842461571425821170776
c2 = 100

# Compute g^x (which is the same as c1 in this case)
gx = public_key

# Calculate the modular inverse of g^x mod p
gx_inv = mod_inverse(gx, p)

# Recover the message m
m = (c2 * gx_inv) % p

print(f"Scenario 2 m : {m}")



###############################################scenario3######################################################

# Define the parameters
g = 5
gx = 1953125
c1 = 15625
c2 = 832667268468867405317723751068115234375

# Check if c1 and gx are coprime
if math.gcd(c1, gx) != 1:
    print(f"scenario 3 : c1 and gx are not coprime; modular inverse does not exist.")
# Calculate the modular inverse of c1 mod gx
else:
    c1_inv = mod_inverse(c1, gx)
    m = (c2 * c1_inv) % gx
    print(f"The decrypted message m is: {m}")

##############################################################scenario4################################################################
p = int("179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503753865831008441973494225499923250055784177410756159608183883985327442870672832045437787739365040606923860277363437139134990143853263608877373248332082093166171808999999")
g = 7

public_key = int("3058843465936720333571907537725961041445031134453247421217185542206828644502906784194608582991418620833696922836830311881252747881608871133767925544901090328582111139148688377491811122951242633999813074099087252076850494427651656770450334365948532267385429949222801830757731142576124548")
c1 = int("73330855740916146039866451341029067140760645910390429209230106550516911504466438328923058185249844928564599320433311362370624303450590310387520157712792451622437642898288798595482625546931933534370505271689851499772227787077899796419929447185618944933985625760186645614061067964804714315")
c2 = int("23817611852541090570125290828834115548322095407545827778109272490358219512895580542655269250789752794176101844937408655750501617781279486874013125242032019811365018873416201884242522404612407005416448968588993784743249351647076271205671486963550181746045366582617470394981029601045001247")

# Step 1: Compute g^(xy) mod p
g_xy_mod_p = pow(c1, public_key, p)  # Using Python's built-in pow function for modular exponentiation

# Step 2: Compute the modular inverse of g^(xy) mod p
g_xy_inverse_mod_p = mod_inverse(g_xy_mod_p, p)

# Step 3: Recover the message m
m = (c2 * g_xy_inverse_mod_p) % p

# Print the recovered message
print("Scenario 4 m:", m)



#################################################scenario5#######################################################


# Define the parameters
# Define the parameters
p = 95768907671470685161834890931411566592455689334949078397684923142851642341551
g = 47884453835735342580917445465705783296227844667474539198842461571425821170776
c1 = 47884453835735342580917445465705783296227844667474539198842461571425821170776
c2 = 720

# Since g^x = 1, and xy = 0, the decryption is simply c2 % p
m = c2 % p

print(f"scenario 5 m is: {m}")






