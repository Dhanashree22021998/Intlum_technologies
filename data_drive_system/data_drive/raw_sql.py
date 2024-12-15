from django.db import connection


def create_folder(name, parent_id, owner_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO data_drive_folder (name, parent_id, owner_id)
            VALUES (%s, %s, %s)
        """, [name, parent_id, owner_id])


def get_subfolders(folder_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, name, parent_id
            FROM data_drive_folder
            WHERE parent_id = %s
        """, [folder_id])
        return cursor.fetchall()


def update_folder_name(folder_id, new_name):
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE data_drive_folder
            SET name = %s
            WHERE id = %s
        """, [new_name, folder_id])


def delete_folder_recursive(folder_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            WITH RECURSIVE folder_tree AS (
                SELECT id FROM data_drive_folder WHERE id = %s
                UNION ALL
                SELECT f.id
                FROM data_drive_folder f
                INNER JOIN folder_tree ft ON ft.id = f.parent_id
            )
            DELETE FROM data_drive_folder
            WHERE id IN (SELECT id FROM folder_tree)
        """, [folder_id])
