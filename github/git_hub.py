from flask import Flask, render_template, request, jsonify
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import os
app = Flask(__name__)


# Initialize the KMS client
kms_client = boto3.client('kms', region_name='us-east-1')  # Specify your AWS region
key_id = "your-kms-key-id"  


# Replace with your AWS KMS Key ID
///////
# GitHub token for authentication (optional - here, just for demonstration)
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # If needed, you can use this for GitHub API interaction
@app.route('/')
def index():
    return render_template('index.html')
    
# Encrypt Route
@app.route('/encrypt', methods=['POST'])
def encrypt_key():
    try:
        access_key = request.form.get("access_key")
        if not access_key:
            return jsonify({"error": "Access key is required"}), 400

        response = kms_client.encrypt(
            KeyId=key_id,
            Plaintext=access_key.encode('utf-8')
        )

        encrypted_access_key = response['CiphertextBlob']
        return jsonify({"encrypted_access_key": encrypted_access_key.decode('utf-8')}), 200

    except (NoCredentialsError, PartialCredentialsError):
        return jsonify({"error": "AWS credentials not found or incomplete"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Decrypt Route provided
@app.route('/decrypt', methods=['POST'])
def decrypt_key():
    try:
        encrypted_access_key = request.form.get("encrypted_access_key")
        if not encrypted_access_key:
            return jsonify({"error": "Encrypted access key is required"}), 400

        encrypted_bytes = bytes(encrypted_access_key, 'utf-8')

        response = kms_client.decrypt(CiphertextBlob=encrypted_bytes)
        decrypted_access_key = response['Plaintext'].decode('utf-8')

        # In this case, we assume the access key is valid
        # If you want to further validate the access key, you can skip this part.
        return jsonify({"decrypted_access_key": decrypted_access_key}), 200

    except (NoCredentialsError, PartialCredentialsError):
        return jsonify({"error": "AWS credentials not found or incomplete"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Check if GitHub token is available in environment variables
    if not GITHUB_TOKEN:
        GITHUB_TOKEN = input("Please enter your GitHub token (optional): ")

    app.run(debug=True)
