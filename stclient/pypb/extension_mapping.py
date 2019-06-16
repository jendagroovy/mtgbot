def construct_extension_mapping(message_types):
    mapping = {}

    for message_type in message_types:
        extensions = message_type.DESCRIPTOR.file.pool.FindAllExtensions(
            message_type.DESCRIPTOR
        )
        for extension in extensions:
            mapping[extension.extension_scope] = message_type.DESCRIPTOR.name

    return mapping