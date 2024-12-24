import ml_collections
import torch


def get_default_configs():
  config = ml_collections.ConfigDict()
  # training
  config.training = training = ml_collections.ConfigDict()
  config.training.batch_size = 1 #1
  training.n_iters = 1000001
  training.snapshot_freq = 10000#10000#10000 #50000
  training.log_freq = 1
  training.eval_freq = 1
  ## store additional checkpoints for preemption in cloud computing environments
  training.snapshot_freq_for_preemption = 5000
  ## produce samples at each snapshot.
  training.snapshot_sampling = True
  training.likelihood_weighting = False
  training.continuous = True
  training.reduce_mean = False

  # sampling
  config.sampling = sampling = ml_collections.ConfigDict()
  sampling.n_steps_each = 1
  sampling.noise_removal = True
  sampling.probability_flow = False
  sampling.snr = 0.075

  # evaluation
  config.eval = evaluate = ml_collections.ConfigDict()
  evaluate.begin_ckpt = 1
  evaluate.end_ckpt = 100
  evaluate.batch_size = 1
  evaluate.enable_sampling = True
  evaluate.num_samples = 1000    #1000 #50000
  evaluate.enable_loss = True
  evaluate.enable_bpd = False
  evaluate.bpd_dataset = 'test'

  # data
  config.data = data = ml_collections.ConfigDict()
  data.dataset = 'LSUN'
  data.image_size =256
  data.random_flip = False  #True
  data.uniform_dequantization = False
  data.centered = False ### inverse scale / get_data_scaler
  data.num_channels = 1

  # model
  ## train 378     test:1
  config.model = model = ml_collections.ConfigDict()
  model.sigma_max = 1
  model.sigma_min = 1
  model.num_scales = 1
  model.beta_min = 1
  model.beta_max = 1
  model.dropout = 1
  model.embedding_type = 'fourier'

  # optimization
  config.optim = optim = ml_collections.ConfigDict()
  optim.weight_decay = 0
  optim.optimizer = 'Adam'
  optim.lr = 2e-4
  optim.beta1 = 0.9
  optim.eps = 1e-8
  optim.warmup = 5000
  optim.grad_clip = 1.

  config.seed = 42
  config.device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

  return config
