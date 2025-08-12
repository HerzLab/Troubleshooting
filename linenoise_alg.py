def RunLineNoise(eeg, sr, durr_s):
  def RunAnalysis(eeg, sr, durr_s, target_freq):
    if (sr/target_freq)%1 != 0:
      raise ValueError(
          f'{sr}Hz not evenly divisible into {target_freq}Hz windows')
    timebin_len = sr//target_freq   # 50ms for 20Hz, in sample units
    target_timelen = eeg.data.shape[2] if durr_s is None \
        else round(durr_s * sr)
    timebin_cnt = target_timelen//timebin_len
    time_len = timebin_cnt * timebin_len
    # For all channels.
    sel_data = eeg.data[0][:,sr:sr+time_len]
    resh_data = np.reshape(sel_data, (sel_data.shape[0], -1, timebin_len))
    binned = np.mean(resh_data, axis=1)
    stddev = np.std(resh_data, axis=1, ddof=1)
    stderr = sp.stats.sem(resh_data, axis=1, ddof=1)
    bin_sd = np.std(binned, axis=1, ddof=1)
    sel_sd = np.std(sel_data, axis=1, ddof=1)
    line_frac = bin_sd / sel_sd
    return timebin_len, binned, stderr, line_frac

  res50Hz = RunAnalysis(eeg, sr, durr_s, 25)
  res60Hz = RunAnalysis(eeg, sr, durr_s, 20)
  if max(res50Hz[3]) > max(res60Hz[3]):
    res = res50Hz
  else:
    res = res60Hz

# Use like:
#
# timebin_len, binned, stderr, line_frac = RunLineNoise(eeg, eeg.samplerate, 30)

