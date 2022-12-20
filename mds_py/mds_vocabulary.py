class Vocabulary:
    OK = 'OK'
    
    MDS_PY = 'MDS_PY'
    BOOTSTRAP = 'bootstrap'
    CONFIG = 'config'
    PROCESSORS = 'processors'
    SCHEMAS = 'schemas'
    SCRIPTS = 'scripts'
    SQLITE_FILES = 'sqlite_files'

    # Core schemas
    IDX_REG = 'idx_reg'
    CONFIG_FILE = 'config'
    TRANSACTION = 'transaction'
    COMMIT = 'commit'

    # Schema top properties
    ID = '__id'
    NAME = 'name'
    NAMESPACE = 'namespace'
    PREFIX = 'prefix'
    LABEL = 'label'
    KIND = 'kind'
    KEYS = 'keys'
    PROPS = 'props'
    SOURCE = 'source'
    DOC = 'doc'

    # TRANSACTION
    ITEM_ID = 'item_id'
    ITEM_PREFIX = 'item_prefix'
    PROCESSOR_ID ='processor_id'
    PROCESSOR_UUID = 'processor_uuid'
    PROCESSOR_PREFIX = 'processor_prefix'

    # Processing status    
    STATUS = 'status'
    WAITING = 'waiting'
    IN_PROCESS = 'in_process'
    LOCKED = 'locked'
    COMPLETE = 'complete'
    FAILED = 'failed'

    #  redis params
    REDIS = 'redis'
    REDIS_HOST = 'host'
    REDIS_PORT = 'port'