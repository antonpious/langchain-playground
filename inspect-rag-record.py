# local imports
from pineconeclient import pineconeIndex
from settings import Settings

# find how many records
# TODO Filter By Name space
# print(pineconeIndex.describe_index_stats())

# There is no API reference for Python
# most references are JS, JAVA
# https://docs.pinecone.io/reference/api/2025-04/data-plane/describenamespace
# print(pineconeIndex.describe_namespace(Settings.pineCone.ragNamespace))

index = pineconeIndex
namespace = Settings.pineCone.ragNamespace

# These records are too big to display by print
for ids in index.list(namespace=namespace):
    query = index.query(
        id=ids[0], 
        namespace=namespace, 
        top_k=1,
        include_values=True,
        include_metadata=True
    )
    # print(query)
    print(query["matches"][0]["metadata"])
    print("\n")

'''
                        0.0182626918,
                         0.00386541639,
                         -0.0136209913,
                         -0.00724265398]}],
 'namespace': 'tenant3',
 'usage': {'read_units': 6}}

'''


results = {'matches': [{'id': '8a7e5227-a738-4422-9c25-9a6136825803',
            'metadata': {'Header 2': 'Introduction',
                        'text': '## Introduction  \n'
                                'Welcome to the whimsical world of the '
                                'WonderVector5000, an astonishing leap into '
                                'the realms of imaginative technology. This '
                                'extraordinary device, borne of creative '
                                'fancy, promises to revolutionize '
                                'absolutely nothing while dazzling you with '
                                "its fantastical features. Whether you're a "
                                'seasoned technophile or just someone '
                                'looking for a bit of fun, the '
                                'WonderVector5000 is sure to leave you '
                                "amused and bemused in equal measure. Let's "
                                'explore the incredible, albeit entirely '
                                'fictitious, specifications, setup process, '
                                'and troubleshooting tips for this marvel '
                                'of modern nonsense.'},
            'score': 1.0080868,
            'values': [-0.00798303168,
                       0.00551192369,
                       -0.00463955849,
                       -0.00585730933
                      ]}],
'namespace': 'wondervector5000',
'usage': {'read_units': 6}}


print(results["matches"][0]["metadata"])

