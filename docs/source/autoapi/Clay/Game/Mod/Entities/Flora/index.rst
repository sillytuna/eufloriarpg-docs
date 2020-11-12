
Flora Class
===========



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`
* :dn:cls:`Clay.Game.Mod.Entities.Flora`




Syntax
------

.. code-block:: csharp

    public class Flora : Entity, IComparable, IAudioSourceInfo, ITargettable





.. dn:class:: Clay.Game.Mod.Entities.Flora
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Flora


Constructors
------------

.. dn:class:: Clay.Game.Mod.Entities.Flora
    :noindex:
    :hidden:

    .. dn:constructor:: Clay.Game.Mod.Entities.Flora.Flora()




        .. code-block:: csharp

            public Flora()



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Flora
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Flora.Activate(System.String, Clay.Game.Mod.Entities.PlantRootHint, Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type def: System.String

        :type finder: Clay.Game.Mod.Entities.PlantRootHint

        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public void Activate(string def, PlantRootHint finder, Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.ActivateAbilityTree(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void ActivateAbilityTree(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.ActivateArtifactTree(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void ActivateArtifactTree(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.ActivateCollectionTree(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void ActivateCollectionTree(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.ActivateTerraformTree(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void ActivateTerraformTree(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.AddEntity(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public void AddEntity(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.AddHeadLeaf(FloraLeaf)



        :type leaf: FloraLeaf


        .. code-block:: csharp

            public void AddHeadLeaf(FloraLeaf leaf)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.AgeFlora(System.Single, System.Boolean)



        :type time: System.Single

        :type quiet: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool AgeFlora(float time, bool quiet = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.ArtifactFinalizer(System.String)



        :type artifactType: System.String


        .. code-block:: csharp

            public void ArtifactFinalizer(string artifactType)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.AutoLevelUp()




        .. code-block:: csharp

            public void AutoLevelUp()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.BankEnergy(FloraLeaf, System.Int32, System.Boolean)



        :type leaf: FloraLeaf

        :type amount: System.Int32

        :type quietly: System.Boolean


        .. code-block:: csharp

            public void BankEnergy(FloraLeaf leaf, int amount, bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.CanCollectKey(Clay.Game.Mod.Entities.Key)



        :type key: Clay.Game.Mod.Entities.Key

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool CanCollectKey(Key key)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.CleanUpLevel()




        .. code-block:: csharp

            public static void CleanUpLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.CleanUpScripts()




        .. code-block:: csharp

            protected override void CleanUpScripts()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.CollectKey(Clay.Game.Mod.Entities.Key, System.Boolean)



        :type key: Clay.Game.Mod.Entities.Key

        :type quietly: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool CollectKey(Key key, bool quietly)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.CollectingKey(Clay.Game.Mod.Entities.Key)



        :type key: Clay.Game.Mod.Entities.Key


        .. code-block:: csharp

            public void CollectingKey(Key key)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.DamagedBy(Clay.Game.Mod.Entities.Entity, System.Single, Weapon, System.Boolean, System.Boolean)



        :type attacker: Clay.Game.Mod.Entities.Entity

        :type damage: System.Single

        :type weapon: Weapon

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool DamagedBy(Entity attacker, float damage, Weapon weapon, bool effectHandled = false, bool fxHandled = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.DeactivateAbilityTree(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void DeactivateAbilityTree(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.DeactivateArtifactTree(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void DeactivateArtifactTree(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.DeactivateCollectionTree(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void DeactivateCollectionTree(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.DeactivateTerraformTree(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void DeactivateTerraformTree(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.DefensiveResponse()




        .. code-block:: csharp

            public void DefensiveResponse()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.Die(System.Boolean, System.Boolean, System.Boolean)



        :type exploded: System.Boolean

        :type trash: System.Boolean

        :type quietly: System.Boolean


        .. code-block:: csharp

            public override void Die(bool exploded = false, bool trash = true, bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.FindBranches()



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{FloraBranch<FloraBranch>}

        .. code-block:: csharp

            public List<FloraBranch> FindBranches()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.FindElements()



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{FloraElement<FloraElement>}

        .. code-block:: csharp

            public List<FloraElement> FindElements()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.FindLeaves()



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{FloraLeaf<FloraLeaf>}

        .. code-block:: csharp

            public List<FloraLeaf> FindLeaves()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.FindMatureSeedlingLeaves()



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{FloraLeaf<FloraLeaf>}

        .. code-block:: csharp

            public List<FloraLeaf> FindMatureSeedlingLeaves()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.FindSeedlingLeaves()



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{FloraLeaf<FloraLeaf>}

        .. code-block:: csharp

            public List<FloraLeaf> FindSeedlingLeaves()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.ForceSpawn()



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool ForceSpawn()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.FreeBankingEnergy(FloraLeaf, System.Int32)



        :type leaf: FloraLeaf

        :type amount: System.Int32


        .. code-block:: csharp

            public void FreeBankingEnergy(FloraLeaf leaf, int amount)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.FreeKey(Clay.Game.Mod.Entities.Key)



        :type key: Clay.Game.Mod.Entities.Key


        .. code-block:: csharp

            public void FreeKey(Key key)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.GetCommandLine(System.Boolean)



        :type multiLine: System.Boolean

        :rtype: System.String

        .. code-block:: csharp

            public override string GetCommandLine(bool multiLine)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.GetGroup(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity

        :rtype: AIGroup

        .. code-block:: csharp

            public AIGroup GetGroup(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.GetRandomLivingLeaf()



        :rtype: FloraLeaf

        .. code-block:: csharp

            public FloraLeaf GetRandomLivingLeaf()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.GetRandomMatureLeaf()



        :rtype: FloraLeaf

        .. code-block:: csharp

            public FloraLeaf GetRandomMatureLeaf()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.GetRespawnString()



        :rtype: System.String

        .. code-block:: csharp

            public override string GetRespawnString()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.InitialiseMod()




        .. code-block:: csharp

            public static void InitialiseMod()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.InitialiseScripts(System.Boolean)



        :type rebuild: System.Boolean


        .. code-block:: csharp

            protected override void InitialiseScripts(bool rebuild)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.IsDefenseEntityTargetValidCB(Clay.Game.Mod.Entities.Entity, UnityEngine.Vector2)



        :type target: Clay.Game.Mod.Entities.Entity

        :type sourcePosition: UnityEngine.Vector2

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsDefenseEntityTargetValidCB(Entity target, Vector2 sourcePosition)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.IsSpecies(System.String, System.Boolean)



        :type type: System.String

        :type inherited: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsSpecies(string type, bool inherited = true)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.IsSpecies(Tuna.QuickHash, System.Boolean)



        :type typeHash: Tuna.QuickHash

        :type inherited: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsSpecies(QuickHash typeHash, bool inherited = true)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.Rebuild()




        .. code-block:: csharp

            public void Rebuild()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.RebuildLeafSprites()




        .. code-block:: csharp

            public void RebuildLeafSprites()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.RebuildPrototype()




        .. code-block:: csharp

            public override void RebuildPrototype()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.RecalculateExtents()




        .. code-block:: csharp

            protected override void RecalculateExtents()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.RegisterGift(PlayerPaths, System.String, System.String)



        :type path: PlayerPaths

        :type item: System.String

        :type message: System.String


        .. code-block:: csharp

            public static void RegisterGift(PlayerPaths path, string item, string message)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.Relocate()




        .. code-block:: csharp

            public void Relocate()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.RemoveEntity(Clay.Game.Mod.Entities.Entity)



        :type entity: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public void RemoveEntity(Entity entity)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.Render()




        .. code-block:: csharp

            public override void Render()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.RenderDebug()




        .. code-block:: csharp

            public override void RenderDebug()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.ResetBuffers()




        .. code-block:: csharp

            public static void ResetBuffers()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SetAutoLevelUp(System.Int32)



        :type level: System.Int32


        .. code-block:: csharp

            public void SetAutoLevelUp(int level)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SetFruit(FloraLeaf)



        :type leaf: FloraLeaf


        .. code-block:: csharp

            public void SetFruit(FloraLeaf leaf)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SpawnEntities(System.Int32)



        :type spawnCount: System.Int32


        .. code-block:: csharp

            public void SpawnEntities(int spawnCount)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SpawnEntity()



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity SpawnEntity()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SpawnEntityFromLeaf(FloraLeaf, System.Boolean)



        :type leaf: FloraLeaf

        :type quietly: System.Boolean

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity SpawnEntityFromLeaf(FloraLeaf leaf, bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SpawnEntityFromLeafQuietly(FloraLeaf)



        :type leaf: FloraLeaf

        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity SpawnEntityFromLeafQuietly(FloraLeaf leaf)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SpawnFlora(System.String[])



        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.Flora

        .. code-block:: csharp

            public static Flora SpawnFlora(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SpawnFlora(System.String[], System.Boolean)



        :type parameters: System.String<System.String>[]

        :type checkColonised: System.Boolean

        :rtype: Clay.Game.Mod.Entities.Flora

        .. code-block:: csharp

            public static Flora SpawnFlora(string[] parameters, bool checkColonised)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SpawnFloraLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Flora

        .. code-block:: csharp

            public static Flora SpawnFloraLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SpawnParticlesAtGrowAngle(System.String)



        :type fx: System.String


        .. code-block:: csharp

            public void SpawnParticlesAtGrowAngle(string fx)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SpawnPlayerFlora(System.String[])



        :type parameters: System.String<System.String>[]


        .. code-block:: csharp

            public static void SpawnPlayerFlora(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SpawnPlayerFloraLua(System.String)



        :type parameters: System.String


        .. code-block:: csharp

            public static void SpawnPlayerFloraLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.SuppressedBy(Clay.Game.Mod.Entities.Entity, System.Single, System.Boolean, System.Boolean)



        :type attacker: Clay.Game.Mod.Entities.Entity

        :type time: System.Single

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean


        .. code-block:: csharp

            public override void SuppressedBy(Entity attacker, float time, bool effectHandled = false, bool fxHandled = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.TrySpawn(System.Single, System.Boolean)



        :type time: System.Single

        :type forced: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool TrySpawn(float time, bool forced = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.TrySpawnDefenseTree()



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity TrySpawnDefenseTree()

    .. dn:method:: Clay.Game.Mod.Entities.Flora.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.UpdateGrowth(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public void UpdateGrowth(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.UpdatePersistentEffects(System.Single, System.Boolean)



        :type time: System.Single

        :type fx: System.Boolean


        .. code-block:: csharp

            public override void UpdatePersistentEffects(float time, bool fx)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.WakeUpFlora(System.Boolean)



        :type quietly: System.Boolean


        .. code-block:: csharp

            public void WakeUpFlora(bool quietly = false)

    .. dn:method:: Clay.Game.Mod.Entities.Flora.WeakenedBy(Clay.Game.Mod.Entities.Entity, System.Single, Weapon, System.Boolean, System.Boolean)



        :type attacker: Clay.Game.Mod.Entities.Entity

        :type amount: System.Single

        :type weapon: Weapon

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean


        .. code-block:: csharp

            public override void WeakenedBy(Entity attacker, float amount, Weapon weapon, bool effectHandled = false, bool fxHandled = false)



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Flora
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Flora.Animator



        :rtype: Clay.Game.ObjectAnimator

        .. code-block:: csharp

            public ObjectAnimator Animator { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.ageRatio



        :rtype: System.Single

        .. code-block:: csharp

            public float ageRatio { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.attractiveness



        :rtype: System.Single

        .. code-block:: csharp

            public float attractiveness { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.baseStalk



        :rtype: FloraBranch

        .. code-block:: csharp

            public FloraBranch baseStalk { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.currentLevel



        :rtype: System.Int32

        .. code-block:: csharp

            public int currentLevel { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.currentLevelAge



        :rtype: System.Single

        .. code-block:: csharp

            public float currentLevelAge { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.customLeafType



        :rtype: System.String

        .. code-block:: csharp

            public string customLeafType { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.defensiveReaction



        :rtype: FloraDefensiveReactions

        .. code-block:: csharp

            public FloraDefensiveReactions defensiveReaction { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.floraDef



        :rtype: FloraDef

        .. code-block:: csharp

            public FloraDef floraDef { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.fruitLeaf



        :rtype: FloraLeaf

        .. code-block:: csharp

            public FloraLeaf fruitLeaf { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.growAngle



        :rtype: System.Single

        .. code-block:: csharp

            public float growAngle { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.hasFruited



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool hasFruited { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.headLeaves



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{FloraLeaf<FloraLeaf>}

        .. code-block:: csharp

            public List<FloraLeaf> headLeaves { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isAbilityActive



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isAbilityActive { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isAbilityTree



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isAbilityTree { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isArtifactTree



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isArtifactTree { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isAutoLevelingUp



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isAutoLevelingUp { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isCollectionTree



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isCollectionTree { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isDefense



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDefense { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isDestinationArtifactTree



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDestinationArtifactTree { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isDormant



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDormant { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isDyson



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDyson { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isFlora



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isFlora { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isGrandfatherTree



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isGrandfatherTree { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isHidden



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isHidden { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isLastLevel



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isLastLevel { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isMature



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isMature { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isProtected



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isProtected { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isRelay



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isRelay { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isShrinking



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isShrinking { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isSpawner



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isSpawner { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isStuntable



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isStuntable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isSuppressed



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isSuppressed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isTerraformEnergy



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isTerraformEnergy { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isTerraformSpeed



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isTerraformSpeed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isTerraformStrength



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isTerraformStrength { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.isTerraformTree



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isTerraformTree { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.leafEntity



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity leafEntity { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.levelAgeRatio



        :rtype: System.Single

        .. code-block:: csharp

            public float levelAgeRatio { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.levelGrowthTime



        :rtype: System.Single

        .. code-block:: csharp

            public float levelGrowthTime { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.levelUpTime



        :rtype: System.Single

        .. code-block:: csharp

            public float levelUpTime { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.linkedItemName



        :rtype: System.String

        .. code-block:: csharp

            public string linkedItemName { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.maxEntitiesToSpawnFromFlora



        :rtype: System.Int32

        .. code-block:: csharp

            public int maxEntitiesToSpawnFromFlora { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.maximumLevelReached



        :rtype: System.Int32

        .. code-block:: csharp

            public int maximumLevelReached { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.requiresFullProcessing



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool requiresFullProcessing { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.savedBankedEnergies



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{System.Int32<System.Int32>}

        .. code-block:: csharp

            public List<int> savedBankedEnergies { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.savedBankedEnergyTypes



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{AttributeTypes<AttributeTypes>}

        .. code-block:: csharp

            public List<AttributeTypes> savedBankedEnergyTypes { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.sensibleAiPosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public override Vector2 sensibleAiPosition { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.terraformEnergyTypes



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{AttributeTypes<AttributeTypes>}

        .. code-block:: csharp

            public List<AttributeTypes> terraformEnergyTypes { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.totalBankedEnergy



        :rtype: System.Int32

        .. code-block:: csharp

            public int totalBankedEnergy { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.totalBankingEnergy



        :rtype: System.Int32

        .. code-block:: csharp

            public int totalBankingEnergy { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Flora.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }



