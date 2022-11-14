import sys
import os
import json
try:
    import pandas,web3,numpy,gym
except ImportError:
    import pip 
    pip.main(['install','--user', 'pandas==1.3.3'])
    pip.main(['install','--user', 'web3==5.25.0'])
    pip.main(['install','--user', 'numpy==1.20.3'])
    pip.main(['install','--user', 'gym==0.17.3'])
import web3 
import pandas as pd
from web3 import Web3
import numpy as np
import gym
# import bitfinex
# api_v2 = bitfinex.bitfinex_v2.api_v2()
# result = api_v2.candles()

# print('Downloading the most recent Ethereum data')

# print('DOWNLOADING BITCOIN PAIRS DATA')
# api_v2 = bitfinex.bitfinex_v2.api_v2()
# result = api_v2.candles()
# time_step = 60000000
#  # Define query parameters
# pair = 'btcusd' # Currency pair of interest
# bin_size = '1m' # This will return minute data
# limit = 1000    # We want the maximum of 1000 data points
# # Define the start date
# t_start = datetime.datetime(2021,11, 12,0, 0)
# t_start = time.mktime(t_start.timetuple()) * 1000
# # Define the end date
# t_stop = datetime.datetime(2021,11, 13, 0, 0)
# t_stop = time.mktime(t_stop.timetuple()) * 1000
# result = api_v2.candles(symbol=pair, interval=bin_size,
#                         limit=limit, start=t_start, end=t_stop)
# # result =  pd.DataFrame(list_of_rows,columns=['PRICES','PRICE:'])
# def fetch_data(start, stop, symbol, interval, tick_limit, step):
#     api_v2 = bitfinex.bitfinex_v2.api_v2()
#     data = []
#     start = start - step
#     while start < stop:
#         start = start + step
#         end = start + step
#         res = api_v2.candles(symbol=symbol, interval=interval,
#                              limit=tick_limit, start=start,
#                              end=end)
#         data.extend(res)
#         time.sleep(2)
#     return data
# api_v1 = bitfinex.bitfinex_v1.api_v1()
# pairs = ['ethusd']#api_v1.symbols() #['btcusd','xtzusd','oxtusd','dntusd','xtzusd','xrpusd','zecusd','ethusd','etcusd','xlmusd','oxtusd','dntusd','linkusd','eosusd']
# save_path = 'data/crypto/eth'
# if os.path.exists(save_path) is False:
#     os.mkdir(save_path)
# for pair in pairs:
#     pair_data = fetch_data(start=t_start, stop=t_stop, symbol=pair, interval=bin_size, tick_limit=limit, step=time_step)
#     # Remove error messages
#     ind = [np.ndim(x) != 0 for x in pair_data]
#     pair_data = [i for (i, v) in zip(pair_data, ind) if v]
#     #Create pandas data frame and clean data
#     names = ['time', 'open', 'high', 'low', 'close', 'volume']
#     df = pd.DataFrame(pair_data, columns=names)
#     df.drop_duplicates(inplace=True)
#     # df['time'] = pd.to_datetime(df['time'], unit='ms')
#     df.set_index('time', inplace=True)
#     df.sort_index(inplace=True)
#     print('Done downloading data. Saving to .csv.')
#     df.to_csv('{}/bitfinex_eth.csv'.format(save_path, pair))
#     print('Done saving pair{}. Moving to next pair.'.format(pair))
#     # df.drop(['volume'],axis=1)
# print('Done retrieving data')


infura_url = "https://eth-goerli.g.alchemy.com/v2/wz97hc4tHaFJJGcD9nUxC_xyRMaAJjyh"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
true = True
false = False

print('Using Goerli BLCKJK testnet token.')
abi='[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"_setValues","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"compoundFreq","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"compoundRewardsTimer","outputs":[{"internalType":"uint256","name":"_timer","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getDepositInfo","outputs":[{"internalType":"uint256","name":"_stake","type":"uint256"},{"internalType":"uint256","name":"_rewards","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"minStake","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rewardsPerHour","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"s_maxSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"fee","type":"uint256"}],"name":"setFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"setFeeRecipient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"setTokenAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stakeRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawAll","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
abi = json.loads(abi)

#Staking Contract
address = "0x3E485c8955e2F611AAD8a68a30F17e83bA9eAd0d" 
print("creating BLJK token smart contract instance.")
contract = web3.eth.contract(address=address, abi=abi)

bljk_dealer = '0x8c69A67e016Bd3BDcbCCb813EcEd93CeFd3c9908'
print("BLJK tokens in Dealer's wallet {}".format(contract.functions.balanceOf(bljk_dealer).call()))


#House Initialization of House contract instance
balance1 = web3.eth.getBalance(bljk_dealer)
print(web3.fromWei(balance1, "ether"))


# market = pd.read_csv('data/crypto/eth/bitfinex_eth.csv')
# shares1 = balance1
# print('Current Ethereum Portfolio')
# cap = market['open'] * shares1

web3.eth.acct = '0x8c69A67e016Bd3BDcbCCb813EcEd93CeFd3c9908' ## 21 House Wallet
house_account = web3.eth.acct

true = True
false = False

players= '1' #input('how many players ?')


##Inititalize dAIsy21 Blackjack Environment

env = gym.make('Blackjack-v0')
obs_space = env.observation_space
act_space = env.action_space
print(obs_space)
print(act_space)
print('AGENT HAS {} POTENTIAL ACTIONS'.format(act_space))
print('dAIsy21 ^__^')

def generate_episode_from_limit(bljck_env):
    episode = []
    state = bljck_env.reset()
    while True:
        action = 0 if state[0] >18 else 1
        next_state, reward, done, info = bljck_env.step(action)
        episode.append((state,action,reward))
        state = next_state
        if done:
            print('THE GAME IS OVER !', reward)
            print('PLAYER WON THE GAME ^____^ \n') if reward >0 else print('THE AGENT WONT THE GAME  X__x')
            break
    return episode
for i in range(21):
    print(generate_episode_from_limit(env))

def latest_block():
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    web3.eth.getBlock('latest')
    a = web3.eth.getBlock('latest')
    b = print(a)
    return b 


from collections import defaultdict
import numpy as np
import sys
act_space = env.action_space
def monte(env,num_episodes, gen_ep, gamma=.65):
    if players == '1':
        p1 = input('enter ethereum address , ily its all fun and games') #'ENTER PLAYER WALLET' 
        p1_key = input('enter private key, EVERYTHING IS LOCAL WITH NO DATABASE')#'ENTER PLAYER PRIVATE KEY'
        returns = defaultdict(list)
        for i_episode in range(1,num_episodes+1):
            if i_episode % 1000 == 0:
                print('\rEpisode {}/{}'.format(i_episode,num_episodes), end=' ')
                sys.stdout.flush()
                
            # num_episodes = HOW MANY ROUNDS / DQN Learning iterations  ??
            num_episodes = 10000
            for i_episode in range(num_episodes):
                done = False
                s_0 = env.reset()
                gen_ep = []

                state = [s_0]
                while done == False:
                    # Implement policy
                    if s_0[0] >= 18:
                        s_1, reward, done, info = env.step(0)
                    else:
                        s_1, reward,done, info = env.step(1)

                    gen_ep.append((reward*gamma,state))
                    returns.get(reward)
                    print(gen_ep,'\n')
                    state.append((s_0,reward))
                    latest_block()
                    

                    if done == True and reward>0*gamma:
                        print('\n\n\n\n\n\n')
                        print('done \n',reward*gamma)
                        print('\n\n\n\n\n\n')
                        print('21 bust house wins:',reward*gamma)
                        nonce = web3.eth.getTransactionCount(p1) 
                        ## SENDING 100 TOKENS TO HOUSE, PLAYER LOST
                        tx = contract.functions.transferFrom(p1,bljk_dealer,100000000000000000000).buildTransaction({'chainId':5, 'gas':275000, 'nonce':nonce})
                        print('\n\n\n\n\n\n')
                        print(tx)
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        signed_tx = web3.eth.account.signTransaction(tx,str(p1_key))
                        print(signed_tx)
                        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        print('Current Balance {}'.format(shares1))
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                        latest_block()
                    else:
                        print('\n\n\n\n\n\n')
                        print('21 bust dAIsy wins:',reward*gamma)
                        break
                        continue
                        for s_i, s in i_episode(state[:-1]):
                            Vs = np.average(gen_ep[s_i:])*gamma
                            print('Vs:',Vs)
                            # print('Current Balance {}'.format(shares1))
                        break

            return

print(monte(env,10,gen_ep=generate_episode_from_limit))
