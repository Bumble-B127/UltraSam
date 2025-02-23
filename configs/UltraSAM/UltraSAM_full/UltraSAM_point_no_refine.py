_base_ = ['../../_base_/datasets/sam_dataset.py', '../../_base_/models/sam.py']

data_root = 'UltraSAM_DATA'

train_dataloader = dict(
    batch_size=8,
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img=''),
        ann_file='train.agnostic.noSmall.coco.json',
    ),
)

val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img=''),
        ann_file='val.agnostic.noSmall.coco.json',
    ),
)

test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        data_prefix=dict(img=''),
        ann_file='test.agnostic.noSmall.coco.json',
    ),
)

orig_val_evaluator = _base_.val_evaluator
orig_val_evaluator[0]['ann_file'] = '{}/test.agnostic.noSmall.coco.json'.format(data_root)
val_evaluator = orig_val_evaluator

orig_test_evaluator = _base_.test_evaluator
orig_test_evaluator[0]['ann_file'] = '{}/test.agnostic.noSmall.coco.json'.format(data_root)
test_evaluator = orig_test_evaluator
