################################################################################################################
#
# https://cynthiakiser.com/blog/2022/01/06/trimming-wagtail-migration-cruft.html
#
# Remove the database field definition override that Wagtail adds to StreamFields. It creates unnecessary churn
# in our migration files that ends up being really annoying.
################################################################################################################
import wagtail.fields


def deconstruct_without_block_definition(self):
    name, path, _, kwargs = super(wagtail.fields.StreamField, self).deconstruct()
    block_types = list()
    args = [block_types]
    return name, path, args, kwargs


wagtail.fields.StreamField.deconstruct = deconstruct_without_block_definition


print("[WARNING] Django and wagtail has been patched :-)")
