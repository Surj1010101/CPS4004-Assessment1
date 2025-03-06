from database import db_setup
from models import claim, policy

def main():
    db_setup.main()


    conn = claim.create_connection("global_insurance.db")
    with conn:
        new_claim = ('12345', '2025-03-04', 'Accident', 'Car accident on highway')
        claim_id = claim.add_claim(conn, new_claim)
        print(f"Claim added with id: {claim_id}")

        updated_claim = ('12345', '2025-03-04', 'Accident', 'Updated description', claim_id)
        claim.update_claim(conn, updated_claim)
        print(f"Claim updated with id: {claim_id}")


    conn = policy.create_connection("global_insurance.db")
    with conn:
        new_policy = ('POL12345', 'Full Coverage', '100000')
        policy_id = policy.add_policy(conn, new_policy)
        print(f"Policy added with id: {policy_id}")

        updated_policy = ('POL12345', 'Full Coverage', '150000', policy_id)
        policy.update_policy(conn, updated_policy)
        print(f"Policy updated with id: {policy_id}")

if __name__ == "__main__":
    main()