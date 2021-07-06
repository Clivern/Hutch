# Copyright 2022 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes


class SSH:
    """SSH Service"""

    def generate(self):
        # generate new RSA key pair
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

        # serialize private key to PEM format
        private_key = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )

        # serialize public key to OpenSSH format
        public_key = key.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH,
        )

        # convert byte strings to regular strings
        private_key_str = private_key.decode("utf-8")
        public_key_str = public_key.decode("utf-8")

        return {
            "private_key": private_key_str,
            "public_key": public_key_str,
        }
