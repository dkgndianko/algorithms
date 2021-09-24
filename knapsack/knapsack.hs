knapsack :: (Real a, Show b) => a -> [(b, a, a)] -> (a, a, [(b, Bool)])
knapsack t [] = (0, 0, [])
knapsack t [(i, w, v)] = if (w <= t) then (v, w, [(i, True)]) else (0, 0, [(i, False)])
knapsack t all@((i, w, v):xs)
	| (t <= 0)			= (0, 0, [(e, False) | (e, _, _) <- all])
	| (w > t) 			= (t2, w2, (i, False):r2)
	| (t1 + v >= t2)	= (t1 + v, w1 + w,  (i, True):r1)
	| otherwise			= (t2, w2, (i, False):r2)
	-- the two above guards can be replaced by this bottom line
	-- | otherwise = if (t1 + v >= t2) then (t1 + v, w1 + w,  (i, True):r1) else (t2, w2, (i, False):r2)
	where	(t1, w1, r1) = (knapsack (t-w) xs);
			(t2, w2, r2) = (knapsack t xs)

-- exemple of usage
--knapsack 11 [(2, 3, 4), (3, 4, 5), (4, 5, 6)]