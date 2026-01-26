function isOrderedEnvs(env e1, env e2) returns bool {
    return (e1.block.number < e2.block.number && e1.block.timestamp < e2.block.timestamp) || 
           (e1.block.number == e2.block.number && e1.block.timestamp == e2.block.timestamp);
}
