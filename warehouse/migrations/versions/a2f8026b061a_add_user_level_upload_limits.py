# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
add user level upload limits

Revision ID: a2f8026b061a
Revises: aa3a4757f33a
Create Date: 2022-11-22 14:33:56.405811
"""

import sqlalchemy as sa

from alembic import op

revision = "a2f8026b061a"
down_revision = "aa3a4757f33a"


def upgrade():
    op.add_column("users", sa.Column("upload_limit", sa.Integer(), nullable=True))
    op.add_column(
        "users", sa.Column("total_size_limit", sa.BigInteger(), nullable=True)
    )


def downgrade():
    op.drop_column("users", "total_size_limit")
    op.drop_column("users", "upload_limit")
